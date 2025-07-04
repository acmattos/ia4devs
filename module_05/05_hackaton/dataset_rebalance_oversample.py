import os
import shutil
import random
import cv2
import numpy as np
from collections import defaultdict, Counter

# --- Configuração de caminhos e parâmetros ---
BASE_DIR     = 'data/dataset/aws'
SPLITS       = ['train', 'valid', 'test']
MIN_VALID    = 5       # mínimo de imagens por classe em valid
MIN_TEST     = 5       # mínimo de imagens por classe em test
TARGET_TRAIN = 50      # meta de imagens por classe em train
# -------------------------------------------

# Diretórios por split
paths = {
    split: {
        'images': os.path.join(BASE_DIR, split, 'images'),
        'labels': os.path.join(BASE_DIR, split, 'labels')
    }
    for split in SPLITS
}

# Extensões de imagem suportadas
IMG_EXTS = ['.jpg', '.jpeg', '.png']


def load_class_files(split):
    """
    Retorna contagem e arquivos base por classe no split.
    """
    cnt = Counter()
    class_files = defaultdict(set)
    lbl_dir = paths[split]['labels']
    for fn in os.listdir(lbl_dir):
        if not fn.endswith('.txt'):
            continue
        base = os.path.splitext(fn)[0]
        with open(os.path.join(lbl_dir, fn), 'r') as f:
            for line in f:
                cls = int(line.split()[0])
                cnt[cls] += 1
                class_files[cls].add(base)
    return cnt, class_files


def find_image(base, split):
    """
    Encontra imagem correspondente ao base em split, retorna caminho ou None.
    """
    img_dir = paths[split]['images']
    for ext in IMG_EXTS:
        candidate = os.path.join(img_dir, base + ext)
        if os.path.exists(candidate):
            return candidate
    return None


def move_pair(base, src_split, dst_split):
    """
    Move par imagem+label de src_split para dst_split.
    """
    # Move imagem
    src_img = find_image(base, src_split)
    if src_img:
        dst_img = os.path.join(paths[dst_split]['images'], os.path.basename(src_img))
        shutil.move(src_img, dst_img)
    # Move label
    src_lbl = os.path.join(paths[src_split]['labels'], base + '.txt')
    if os.path.exists(src_lbl):
        dst_lbl = os.path.join(paths[dst_split]['labels'], base + '.txt')
        shutil.move(src_lbl, dst_lbl)


def photometric_augment(image):
    """
    Aplica brilho/contraste e ruído gaussiano à imagem, mantendo boxes.
    """
    alpha = random.uniform(0.8, 1.2)
    beta = random.uniform(-20, 20)
    aug = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    noise = np.random.normal(0, 10, aug.shape).astype(np.uint8)
    aug = cv2.add(aug, noise)
    return aug


if __name__ == '__main__':
    random.seed(42)

    # Carrega contagens e arquivos por split
    split_counts = {}
    split_files = {}
    for split in SPLITS:
        cnt, files = load_class_files(split)
        split_counts[split] = cnt
        split_files[split] = files

    moved_valid = moved_test = oversampled = 0

    # Itera sobre todas as classes encontradas em qualquer split
    all_classes = set().union(*[counts.keys() for counts in split_counts.values()])
    for cls in all_classes:
        # Determine split de origem com mais instâncias para essa classe
        counts = {split: split_counts[split].get(cls, 0) for split in SPLITS}
        src_candidates = {s: c for s, c in counts.items() if s != 'train' and c > 0}
        # Source best for non-train splits
        src_best_non_train = max(src_candidates, key=src_candidates.get) if src_candidates else None
        # --- Ensure minimum in train from non-train source if empty ---
        need_train_min = max(0, MIN_VALID - split_counts['train'].get(cls, 0))
        if need_train_min > 0 and src_best_non_train:
            avail = list(split_files[src_best_non_train].get(cls, []))
            random.shuffle(avail)
            for base in avail[:need_train_min]:
                # Augment and copy to train
                img_path = find_image(base, src_best_non_train)
                lbl_path = os.path.join(paths[src_best_non_train]['labels'], base + '.txt')
                if not img_path or not os.path.exists(lbl_path):
                    continue
                img = cv2.imread(img_path)
                aug_img = photometric_augment(img)
                new_base = f"{base}_os_{cls}_{len(split_files['train'][cls])}"
                ext = os.path.splitext(img_path)[1]
                cv2.imwrite(os.path.join(paths['train']['images'], new_base + ext), aug_img)
                shutil.copy(lbl_path, os.path.join(paths['train']['labels'], new_base + '.txt'))
                # update counts
                split_counts['train'][cls] += 1
                split_files['train'][cls].add(new_base)
                oversampled += 1
        # --- Rebalance valid ---
        need_valid = max(0, MIN_VALID - split_counts['valid'].get(cls, 0))
        if need_valid > 0:
            # Preferir mover de 'train', fallback para 'test'
            if split_counts['train'].get(cls, 0) > 0:
                src = 'train'
            elif split_counts['test'].get(cls, 0) > 0:
                src = 'test'
            else:
                src = None
            if src:
                avail = list(split_files[src].get(cls, []))
                random.shuffle(avail)
                for base in avail[:need_valid]:
                    move_pair(base, src, 'valid')
                    moved_valid += 1
                    split_counts['valid'][cls] += 1
                    split_counts[src][cls] -= 1
                    split_files['valid'][cls].add(base)
                    split_files[src][cls].discard(base)
            else:
                print(f"Aviso: sem origem para rebalancear classe {cls} em valid.")

        # --- Rebalance test ---
        need_test = max(0, MIN_TEST - split_counts['test'].get(cls, 0))
        if need_test > 0:
            # Preferir mover de 'train', fallback para 'valid'
            if split_counts['train'].get(cls, 0) > 0:
                src = 'train'
            elif split_counts['valid'].get(cls, 0) > 0:
                src = 'valid'
            else:
                src = None
            if src:
                avail = list(split_files[src].get(cls, []))
                random.shuffle(avail)
                for base in avail[:need_test]:
                    move_pair(base, src, 'test')
                    moved_test += 1
                    split_counts['test'][cls] += 1
                    split_counts[src][cls] -= 1
                    split_files['test'][cls].add(base)
                    split_files[src][cls].discard(base)
            else:
                print(f"Aviso: sem origem para rebalancear classe {cls} em test.")

                # --- Oversample train ---
        count_train = split_counts['train'].get(cls, 0)
        if count_train < TARGET_TRAIN:
            need_os = TARGET_TRAIN - count_train
            # Escolhe fonte para oversample: prioritize train, then test, then valid
            if split_counts['train'].get(cls, 0) > 0:
                src = 'train'
            elif split_counts['test'].get(cls, 0) > 0:
                src = 'test'
            elif split_counts['valid'].get(cls, 0) > 0:
                src = 'valid'
            else:
                src = None
            if not src:
                print(f"Aviso: sem imagens de origem para oversampling da classe {cls}.")
            else:
                bases = list(split_files[src].get(cls, []))
                if not bases:
                    print(f"Aviso: sem imagens base para oversampling da classe {cls} em {src}.")
                else:
                    random.shuffle(bases)
                    for i in range(need_os):
                        base = bases[i % len(bases)]
                        img_path = find_image(base, src)
                        lbl_path = os.path.join(paths[src]['labels'], base + '.txt')
                        if not img_path or not os.path.exists(lbl_path):
                            continue
                        img = cv2.imread(img_path)
                        aug_img = photometric_augment(img)
                        new_base = f"{base}_os_{cls}_{i}"
                        ext = os.path.splitext(img_path)[1]
                        # Salva imagem aumentada em train
                        cv2.imwrite(os.path.join(paths['train']['images'], new_base + ext), aug_img)
                        shutil.copy(lbl_path, os.path.join(paths['train']['labels'], new_base + '.txt'))
                        oversampled += 1
                        split_counts['train'][cls] += 1
                        split_files['train'][cls].add(new_base)

    # Relatório final
    print(f"Rebalance valid: {moved_valid} arquivos movidos")
    print(f"Rebalance test:  {moved_test} arquivos movidos")
    print(f"Oversampled:     {oversampled} imagens geradas")
    print(f"Rebalance valid: {moved_valid} arquivos movidos")
    print(f"Rebalance test:  {moved_test} arquivos movidos")
    print(f"Oversampled:     {oversampled} imagens geradas")