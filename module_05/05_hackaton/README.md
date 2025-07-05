yolo11n
```bash
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton> py .\model.py
New https://pypi.org/project/ultralytics/8.3.162 available  Update with 'pip install -U ultralytics'
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
engine\trainer: agnostic_nms=False, amp=True, augment=True, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data/dataset/aws/data.yaml, degrees=0.0, deterministic=True, dev
ice=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=
1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.001, lrf=0.05, mas
k_ratio=4, max_det=300, mixup=0.5, mode=train, model=./data/model/yolo11n.pt, momentum=0.937, mosaic=1.0, multi_scale=True, name=yolo11n_custom_100, nbs=64, nms=
False, opset=None, optimize=False, optimizer=AdamW, overlap_mask=True, patience=10, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, proje
ct=None, rect=False, resume=False, retina_masks=False, save=True, save_conf=False, save_crop=False, save_dir=C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yol
o11n_custom_100, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, s
how_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None       
Overriding model.yaml nc=80 with nc=182

                   from  n    params  module                                       arguments
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]
  2                  -1  1      6640  ultralytics.nn.modules.block.C3k2            [32, 64, 1, False, 0.25]
  3                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]
  4                  -1  1     26080  ultralytics.nn.modules.block.C3k2            [64, 128, 1, False, 0.25]
  5                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]
  6                  -1  1     87040  ultralytics.nn.modules.block.C3k2            [128, 128, 1, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]
  8                  -1  1    346112  ultralytics.nn.modules.block.C3k2            [256, 256, 1, True]
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]
 10                  -1  1    249728  ultralytics.nn.modules.block.C2PSA           [256, 256, 1]
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 13                  -1  1    111296  ultralytics.nn.modules.block.C3k2            [384, 128, 1, False]
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 16                  -1  1     32096  ultralytics.nn.modules.block.C3k2            [256, 64, 1, False]           
 17                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 19                  -1  1     86720  ultralytics.nn.modules.block.C3k2            [192, 128, 1, False]
 20                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]
 22                  -1  1    378880  ultralytics.nn.modules.block.C3k2            [384, 256, 1, True]
 23        [16, 19, 22]  1    521278  ultralytics.nn.modules.head.Detect           [182, [64, 128, 256]]
YOLO11n summary: 181 layers, 2,680,446 parameters, 2,680,430 gradients, 6.9 GFLOPs

Transferred 448/499 items from pretrained weights
ClearML Task: created new task id=799a905aa2024052b84ed7c861172dae
ClearML results page: https://app.clear.ml/projects/14f0119248fa451f826c387955b212a3/experiments/799a905aa2024052b84ed7c861172dae/output/log
WARNING ClearML Initialized a new task. If you want to run remotely, please add clearml-init and connect your arguments before initializing YOLO.
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
AMP: checks passed 
train: Fast image access  (ping: 0.10.0 ms, read: 306.3170.7 MB/s, size: 416.9 KB)
train: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\train\labels.cache... 5276 images, 0 backgrounds, 0 corrupt: 100%|██
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))
val: Fast image access  (ping: 0.00.0 ms, read: 207.4103.9 MB/s, size: 226.2 KB)
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\labels.cache... 393 images, 0 backgrounds, 0 corrupt: 100%|█████ 
Plotting labels to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\labels.jpg... 
optimizer: AdamW(lr=0.001, momentum=0.937) with parameter groups 81 weight(decay=0.0), 88 weight(decay=0.0005), 87 bias(decay=0.0)
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100
Starting training for 100 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      1/100      5.41G       1.28      3.598     0.9796        428        768:  83%|████████▎ | 551/660 [02:22<00:12,  8.41it/s]ClearML Monitor: Could not detect iteration reporting, falling back to iterations as seconds-from-start
      1/100      5.41G      1.265      3.459     0.9794        147        352: 100%|██████████| 660/660 [02:36<00:00,  4.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:04<00:00,  6.13it/s]
                   all        393       9029      0.514      0.111     0.0812       0.06

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      2/100      4.37G      1.177      2.551     0.9643        505        704:  15%|█▌        | 99/660 [00:11<01:00,  9.32it/s]ClearML Monitor: Reporting detected, reverting back to iteration based reporting
      2/100      4.88G      1.142      2.272     0.9578        249        544: 100%|██████████| 660/660 [01:30<00:00,  7.28it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.18it/s]
                   all        393       9029      0.488      0.304      0.271      0.191

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      3/100      4.13G      1.096      1.875      0.944        299        416: 100%|██████████| 660/660 [01:20<00:00,  8.24it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.49it/s]
                   all        393       9029      0.491      0.462      0.443      0.338

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      4/100      5.26G       1.05      1.605     0.9345        289        736: 100%|██████████| 660/660 [01:15<00:00,  8.72it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.77it/s]
                   all        393       9029      0.683      0.537      0.622       0.49

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      5/100      6.39G      1.025       1.42     0.9225        179        672: 100%|██████████| 660/660 [01:13<00:00,  8.99it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.98it/s]
                   all        393       9029      0.763      0.606       0.73       0.57

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      6/100      5.38G     0.9956      1.296     0.9177        201        704: 100%|██████████| 660/660 [02:12<00:00,  4.98it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.08it/s]
                   all        393       9029      0.729      0.709      0.789      0.618

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      7/100      5.66G      0.975      1.196     0.9189        169        512: 100%|██████████| 660/660 [03:59<00:00,  2.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  2.00it/s]
                   all        393       9029       0.78      0.774      0.859      0.687

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      8/100      5.83G     0.9647      1.119      0.912        127        960: 100%|██████████| 660/660 [04:20<00:00,  2.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  1.99it/s]
                   all        393       9029      0.849       0.83      0.908      0.726

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      9/100       4.4G     0.9469      1.063     0.9064        188        960: 100%|██████████| 660/660 [04:19<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.17it/s]
                   all        393       9029      0.861      0.845      0.922      0.751

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     10/100      5.28G      0.921     0.9857     0.9025        152        352: 100%|██████████| 660/660 [04:19<00:00,  2.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.22it/s]
                   all        393       9029      0.869      0.871      0.937      0.769

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     11/100      5.69G     0.9186     0.9701     0.9031        302        960: 100%|██████████| 660/660 [04:18<00:00,  2.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  2.01it/s]
                   all        393       9029      0.874      0.881      0.939      0.777

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     12/100       5.2G     0.9052     0.9297     0.8941        208        576: 100%|██████████| 660/660 [04:18<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  2.01it/s]
                   all        393       9029      0.905      0.891      0.952      0.793

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     13/100      4.97G     0.8944     0.8946     0.8938        131        576: 100%|██████████| 660/660 [04:17<00:00,  2.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.22it/s]
                   all        393       9029      0.913       0.92      0.962      0.801

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     14/100      5.01G     0.8914     0.8843     0.8911        182        864: 100%|██████████| 660/660 [04:20<00:00,  2.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.17it/s]
                   all        393       9029      0.921      0.924      0.967      0.801

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     15/100       6.3G     0.8722     0.8429     0.8912        149        864: 100%|██████████| 660/660 [04:20<00:00,  2.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.21it/s]
                   all        393       9029      0.895       0.93      0.961      0.803

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     16/100      5.13G     0.8701     0.8235     0.8831        197        544: 100%|██████████| 660/660 [04:15<00:00,  2.58it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  2.03it/s]
                   all        393       9029      0.919      0.952      0.977      0.821

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     17/100      5.98G     0.8689     0.8336      0.888        216        832: 100%|██████████| 660/660 [04:20<00:00,  2.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.15it/s]
                   all        393       9029      0.913      0.949      0.977      0.813

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     18/100      4.83G     0.8492       0.79     0.8872         76        672: 100%|██████████| 660/660 [04:18<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.17it/s]
                   all        393       9029      0.941      0.965      0.983       0.83

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     19/100       5.1G     0.8549     0.7866     0.8842        175        896: 100%|██████████| 660/660 [04:19<00:00,  2.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.19it/s]
                   all        393       9029      0.943      0.946       0.98      0.822

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     20/100      7.46G     0.8422     0.7601     0.8812        203        928: 100%|██████████| 660/660 [04:20<00:00,  2.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  2.00it/s]
                   all        393       9029      0.948      0.963      0.981      0.826

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     21/100      4.79G     0.8346     0.7539     0.8794        142        736: 100%|██████████| 660/660 [04:18<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  2.06it/s]
                   all        393       9029      0.931      0.961      0.978      0.826

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     22/100      4.62G     0.8277     0.7413     0.8787        186        640: 100%|██████████| 660/660 [04:18<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.17it/s]
                   all        393       9029      0.944      0.963      0.985      0.839

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     23/100      6.69G     0.8203     0.7339     0.8773        235        896: 100%|██████████| 660/660 [04:20<00:00,  2.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.15it/s]
                   all        393       9029      0.928      0.952      0.982      0.833

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     24/100       6.1G     0.8174     0.7202     0.8758        281        416: 100%|██████████| 660/660 [04:18<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  2.00it/s]
                   all        393       9029      0.926      0.962      0.983       0.84

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     25/100      4.97G     0.8136     0.7158     0.8748        166        896: 100%|██████████| 660/660 [03:08<00:00,  3.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.53it/s]
                   all        393       9029      0.935      0.961      0.981       0.84

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     26/100      6.37G      0.804     0.7083     0.8716        231        960: 100%|██████████| 660/660 [04:01<00:00,  2.73it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.30it/s]
                   all        393       9029      0.948      0.967      0.986      0.848

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     27/100      4.75G     0.8091     0.6999     0.8729        221        448: 100%|██████████| 660/660 [04:02<00:00,  2.73it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.21it/s]
                   all        393       9029      0.936      0.977      0.987      0.849

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     28/100      6.25G     0.7954     0.6824     0.8708        366        768: 100%|██████████| 660/660 [04:05<00:00,  2.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.46it/s]
                   all        393       9029       0.94      0.969      0.986      0.853

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     29/100      4.39G     0.7993     0.6959     0.8712        219        320: 100%|██████████| 660/660 [04:14<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:13<00:00,  1.88it/s]
                   all        393       9029      0.935      0.979      0.987      0.855

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     30/100      3.82G     0.7986     0.6889      0.868        130        448: 100%|██████████| 660/660 [04:32<00:00,  2.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  1.93it/s]
                   all        393       9029      0.934      0.964      0.982      0.849

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     31/100      4.26G     0.7826     0.6627      0.867        279        320: 100%|██████████| 660/660 [04:13<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.32it/s]
                   all        393       9029      0.947      0.979      0.988      0.861

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     32/100      5.21G     0.7767     0.6512     0.8676        183        672: 100%|██████████| 660/660 [03:44<00:00,  2.95it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.33it/s]
                   all        393       9029      0.956       0.96      0.985      0.863

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     33/100      4.49G     0.7742     0.6541     0.8654        176        640: 100%|██████████| 660/660 [04:10<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.36it/s]
                   all        393       9029      0.956      0.972      0.988      0.865

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     34/100      4.73G     0.7669     0.6388     0.8635        227        768: 100%|██████████| 660/660 [04:07<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.42it/s]
                   all        393       9029      0.956      0.978       0.99      0.869

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     35/100      5.44G     0.7604     0.6312     0.8629        134        320: 100%|██████████| 660/660 [03:00<00:00,  3.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  2.08it/s]
                   all        393       9029       0.95      0.972      0.989      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     36/100      5.48G     0.7661     0.6329     0.8648        125        576: 100%|██████████| 660/660 [02:55<00:00,  3.77it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.98it/s]
                   all        393       9029      0.957      0.964      0.987      0.861

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     37/100      5.89G     0.7645     0.6235     0.8627        196        480: 100%|██████████| 660/660 [03:23<00:00,  3.24it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:12<00:00,  1.95it/s]
                   all        393       9029       0.95      0.975      0.989      0.863

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     38/100      4.91G     0.7576     0.6277     0.8642        266        352: 100%|██████████| 660/660 [02:37<00:00,  4.18it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:03<00:00,  6.70it/s]
                   all        393       9029      0.963      0.972      0.989      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     39/100      5.39G     0.7535     0.6162     0.8624        422        736: 100%|██████████| 660/660 [02:43<00:00,  4.05it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.44it/s]
                   all        393       9029      0.951      0.982      0.989      0.873

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     40/100      5.83G     0.7554      0.621     0.8593        241        480: 100%|██████████| 660/660 [01:20<00:00,  8.20it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:03<00:00,  7.71it/s]
                   all        393       9029      0.956      0.978      0.989      0.869

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     41/100      4.89G     0.7455     0.6096     0.8565        256        704: 100%|██████████| 660/660 [01:19<00:00,  8.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.54it/s]
                   all        393       9029      0.965      0.965      0.989      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     42/100      4.62G     0.7462     0.6132      0.859        250        704: 100%|██████████| 660/660 [01:21<00:00,  8.07it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.05it/s]
                   all        393       9029      0.943      0.971      0.987      0.871

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     43/100      5.29G     0.7453     0.6111     0.8589        227        768: 100%|██████████| 660/660 [01:21<00:00,  8.12it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.26it/s]
                   all        393       9029      0.953      0.973      0.988      0.876

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     44/100      4.96G      0.726     0.5808     0.8559        325        320: 100%|██████████| 660/660 [01:19<00:00,  8.26it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.10it/s]
                   all        393       9029       0.95      0.979      0.988       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     45/100      4.64G     0.7399     0.6007     0.8575        124        480: 100%|██████████| 660/660 [01:21<00:00,  8.09it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.21it/s]
                   all        393       9029      0.943      0.985      0.989       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     46/100      4.17G     0.7312     0.5906     0.8538        218        512: 100%|██████████| 660/660 [01:17<00:00,  8.47it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.85it/s]
                   all        393       9029      0.952      0.979      0.989      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     47/100      5.37G     0.7241     0.5831      0.856        221        800: 100%|██████████| 660/660 [01:21<00:00,  8.06it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.83it/s]
                   all        393       9029      0.965      0.966      0.989      0.879

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     48/100      4.87G      0.721     0.5721     0.8557        143        704: 100%|██████████| 660/660 [01:21<00:00,  8.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.82it/s]
                   all        393       9029      0.948      0.979      0.989      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     49/100      4.16G     0.7269     0.5936     0.8519        205        736: 100%|██████████| 660/660 [01:47<00:00,  6.16it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.24it/s]
                   all        393       9029      0.955      0.978      0.988      0.881

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     50/100      4.42G     0.7214     0.5833     0.8514        216        960: 100%|██████████| 660/660 [01:20<00:00,  8.16it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.82it/s]
                   all        393       9029      0.965      0.977       0.99      0.884

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     51/100      5.02G     0.7133     0.5649     0.8515        172        416: 100%|██████████| 660/660 [01:46<00:00,  6.19it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.68it/s]
                   all        393       9029      0.957      0.987      0.989      0.885

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     52/100      4.74G     0.7117     0.5647     0.8512        323        576: 100%|██████████| 660/660 [02:08<00:00,  5.15it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.38it/s]
                   all        393       9029      0.959      0.975      0.988      0.885

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     53/100      4.72G     0.7015     0.5558     0.8506        188        800: 100%|██████████| 660/660 [01:46<00:00,  6.19it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.69it/s]
                   all        393       9029      0.956      0.972      0.988      0.882

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     54/100      5.61G     0.7063     0.5648     0.8505        271        896: 100%|██████████| 660/660 [01:22<00:00,  8.03it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.78it/s]
                   all        393       9029      0.952      0.977      0.989      0.885

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     55/100       4.6G     0.7044     0.5595     0.8507        223        864: 100%|██████████| 660/660 [01:25<00:00,  7.71it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.55it/s]
                   all        393       9029      0.971      0.961      0.988      0.887

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     56/100      5.02G     0.7042     0.5537     0.8497        192        512: 100%|██████████| 660/660 [01:22<00:00,  7.99it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:04<00:00,  5.43it/s]
                   all        393       9029       0.95      0.985      0.989      0.889

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     57/100      5.37G     0.6962     0.5507     0.8482        301        832: 100%|██████████| 660/660 [02:09<00:00,  5.10it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.22it/s]
                   all        393       9029      0.947      0.985      0.988       0.89

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     58/100      4.65G     0.7083     0.5673     0.8485        187        384: 100%|██████████| 660/660 [01:49<00:00,  6.01it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.41it/s]
                   all        393       9029      0.959      0.981      0.989      0.891

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     59/100      5.35G        0.7     0.5538     0.8499        237        768: 100%|██████████| 660/660 [02:15<00:00,  4.88it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.18it/s]
                   all        393       9029      0.948      0.986      0.989       0.89

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     60/100      4.82G     0.6979     0.5501     0.8465        280        416: 100%|██████████| 660/660 [02:45<00:00,  3.99it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.19it/s]
                   all        393       9029       0.95      0.987      0.989       0.89

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     61/100      5.12G     0.6926     0.5468     0.8467        206        512: 100%|██████████| 660/660 [03:08<00:00,  3.49it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.30it/s]
                   all        393       9029      0.962      0.975       0.99       0.89

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     62/100       5.4G     0.6973     0.5567     0.8443        295        736: 100%|██████████| 660/660 [02:19<00:00,  4.74it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.31it/s]
                   all        393       9029      0.955      0.982      0.989      0.893

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     63/100      7.11G     0.6796     0.5283     0.8437        146        512: 100%|██████████| 660/660 [01:56<00:00,  5.67it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.14it/s]
                   all        393       9029      0.965      0.973       0.99      0.894

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     64/100      5.18G      0.684     0.5233     0.8447        167        320: 100%|██████████| 660/660 [01:36<00:00,  6.82it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.87it/s]
                   all        393       9029      0.962      0.977      0.989      0.894

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     65/100      5.54G      0.676     0.5253     0.8445        170        384: 100%|██████████| 660/660 [01:22<00:00,  8.01it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.47it/s]
                   all        393       9029      0.963      0.977      0.989      0.895

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     66/100      5.24G     0.6772     0.5238     0.8456        237        512: 100%|██████████| 660/660 [01:22<00:00,  7.99it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.35it/s]
                   all        393       9029      0.942      0.987      0.989      0.894

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     67/100      5.62G      0.674     0.5253     0.8434        366        832: 100%|██████████| 660/660 [01:19<00:00,  8.28it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.18it/s]
                   all        393       9029      0.972      0.964      0.989      0.892

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     68/100      6.31G     0.6728     0.5239     0.8438        127        800: 100%|██████████| 660/660 [01:20<00:00,  8.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.56it/s]
                   all        393       9029      0.961      0.967      0.989      0.897

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     69/100       5.1G     0.6736     0.5182     0.8422        227        864: 100%|██████████| 660/660 [01:33<00:00,  7.07it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.95it/s]
                   all        393       9029      0.973      0.962       0.99      0.896

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     70/100      5.09G     0.6684     0.5073      0.843        248        928: 100%|██████████| 660/660 [01:47<00:00,  6.17it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.18it/s]
                   all        393       9029      0.953      0.983      0.989      0.897

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     71/100      6.04G     0.6703     0.5139     0.8406        154        800: 100%|██████████| 660/660 [01:20<00:00,  8.25it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.91it/s]
                   all        393       9029      0.969      0.966      0.989      0.897

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     72/100      4.38G     0.6647     0.5098     0.8403        216        576: 100%|██████████| 660/660 [01:20<00:00,  8.24it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.03it/s]
                   all        393       9029      0.966      0.966      0.989      0.897

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     73/100      5.03G     0.6672     0.5189       0.84        170        736: 100%|██████████| 660/660 [01:19<00:00,  8.25it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.83it/s]
                   all        393       9029      0.972      0.965      0.989      0.898

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     74/100      4.68G      0.667     0.5157     0.8392        307        544: 100%|██████████| 660/660 [01:19<00:00,  8.28it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.63it/s]
                   all        393       9029      0.951      0.986      0.989        0.9

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     75/100      3.88G     0.6586     0.5028     0.8399        265        896: 100%|██████████| 660/660 [01:19<00:00,  8.25it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.08it/s]
                   all        393       9029      0.975      0.966      0.989        0.9

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     76/100      4.73G     0.6592     0.5029     0.8386        267        736: 100%|██████████| 660/660 [01:20<00:00,  8.25it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.91it/s]
                   all        393       9029      0.973      0.968       0.99      0.902

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     77/100      5.02G     0.6507     0.4899     0.8392        192        544: 100%|██████████| 660/660 [03:55<00:00,  2.80it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.30it/s]
                   all        393       9029      0.977      0.966      0.989      0.903

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     78/100      6.17G      0.652     0.4961     0.8369        207        512: 100%|██████████| 660/660 [04:12<00:00,  2.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.12it/s]
                   all        393       9029      0.974      0.965      0.989      0.902

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     79/100       6.4G     0.6556     0.5011     0.8396        265        864: 100%|██████████| 660/660 [04:11<00:00,  2.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.39it/s]
                   all        393       9029      0.975      0.967      0.989      0.902

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     80/100      4.88G     0.6527     0.5092     0.8371        364        512: 100%|██████████| 660/660 [03:10<00:00,  3.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.82it/s]
                   all        393       9029      0.973      0.967      0.989      0.903

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     81/100      4.48G     0.6501     0.4963     0.8367        194        800: 100%|██████████| 660/660 [01:20<00:00,  8.15it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.93it/s]
                   all        393       9029      0.973      0.967      0.989      0.903

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     82/100      4.73G     0.6459     0.4877     0.8361        264        608: 100%|██████████| 660/660 [01:20<00:00,  8.24it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.10it/s]
                   all        393       9029      0.976      0.964      0.989      0.903

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     83/100      4.45G     0.6497     0.4981     0.8362        172        544: 100%|██████████| 660/660 [01:20<00:00,  8.20it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.99it/s]
                   all        393       9029      0.973      0.963       0.99      0.904

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     84/100      4.43G     0.6422     0.4873     0.8356        246        608: 100%|██████████| 660/660 [02:29<00:00,  4.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:09<00:00,  2.71it/s]
                   all        393       9029      0.978      0.964       0.99      0.907

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     85/100       5.2G     0.6449     0.4897     0.8334        293        768: 100%|██████████| 660/660 [02:43<00:00,  4.03it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:13<00:00,  1.91it/s]
                   all        393       9029      0.977      0.964       0.99      0.907

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     86/100      4.36G     0.6423     0.4893     0.8366        152        608: 100%|██████████| 660/660 [02:06<00:00,  5.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.28it/s]
                   all        393       9029      0.974      0.967      0.989      0.907

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     87/100      4.57G     0.6403     0.4827     0.8346        296        928: 100%|██████████| 660/660 [02:55<00:00,  3.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.10it/s]
                   all        393       9029      0.977      0.965      0.989      0.908

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     88/100      5.23G     0.6413     0.4843     0.8357        356        672: 100%|██████████| 660/660 [03:44<00:00,  2.94it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.88it/s]
                   all        393       9029      0.976      0.966      0.989      0.907

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     89/100      4.92G     0.6369      0.483     0.8329        168        640: 100%|██████████| 660/660 [01:34<00:00,  7.02it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.66it/s]
                   all        393       9029      0.975      0.966       0.99      0.908

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     90/100       4.4G     0.6395     0.4895     0.8363        292        672: 100%|██████████| 660/660 [02:05<00:00,  5.25it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:07<00:00,  3.14it/s]
                   all        393       9029      0.971      0.967       0.99      0.909
Closing dataloader mosaic
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     91/100      3.65G     0.4982     0.3127     0.8096         74        832: 100%|██████████| 660/660 [01:53<00:00,  5.79it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.39it/s]
                   all        393       9029      0.977      0.966      0.989      0.908

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     92/100      3.66G       0.48      0.296     0.8045         62        960: 100%|██████████| 660/660 [01:13<00:00,  9.01it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.51it/s]
                   all        393       9029      0.979      0.965      0.989      0.911

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     93/100      3.68G       0.47     0.2943     0.8026         61        352: 100%|██████████| 660/660 [03:46<00:00,  2.91it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.43it/s]
                   all        393       9029       0.98      0.964       0.99      0.914

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     94/100      3.69G     0.4606     0.2827     0.8018         79        672: 100%|██████████| 660/660 [04:05<00:00,  2.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:11<00:00,  2.24it/s]
                   all        393       9029      0.981      0.964       0.99      0.916

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     95/100      3.69G     0.4556     0.2838     0.8004         81        544: 100%|██████████| 660/660 [03:56<00:00,  2.79it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:10<00:00,  2.48it/s]
                   all        393       9029      0.981      0.965       0.99      0.915

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     96/100      3.69G     0.4535     0.2814     0.8006         86        512: 100%|██████████| 660/660 [02:07<00:00,  5.17it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.31it/s]
                   all        393       9029       0.98      0.965       0.99      0.916

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     97/100      3.69G     0.4445     0.2762        0.8         75        416: 100%|██████████| 660/660 [01:17<00:00,  8.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.64it/s]
                   all        393       9029       0.98      0.965       0.99      0.918

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     98/100      3.69G     0.4448     0.2743     0.7989         71        672: 100%|██████████| 660/660 [01:13<00:00,  8.93it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00, 10.46it/s]
                   all        393       9029      0.981      0.966       0.99       0.92

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     99/100      3.69G     0.4407     0.2746     0.7993         80        544: 100%|██████████| 660/660 [01:17<00:00,  8.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.61it/s]
                   all        393       9029      0.981      0.965       0.99       0.92

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    100/100      3.69G     0.4388     0.2693     0.7976         75        960: 100%|██████████| 660/660 [02:25<00:00,  4.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.55it/s]
                   all        393       9029      0.981      0.965       0.99      0.921

100 epochs completed in 4.609 hours.
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\weights\last.pt, 5.7MB
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\weights\best.pt, 5.7MB

Validating C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\weights\best.pt...
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11n summary (fused): 100 layers, 2,672,434 parameters, 0 gradients, 6.8 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:05<00:00,  4.70it/s]
                   all        393       9029       0.98      0.966       0.99      0.896
                   ACM         40         40      0.995          1      0.995      0.933
                   ALB         67         83      0.988          1      0.995      0.846
                   AMI          7         12       0.98          1      0.995      0.956
           API-Gateway        200        304      0.997      0.988      0.995      0.909
Active Directory Service         36         36      0.994          1      0.995       0.97
              Airflow_          3          6      0.965          1      0.995      0.895
               Amplify         16         16      0.988          1      0.995      0.804
    Analytics Services          5          5      0.967          1      0.995      0.903
               AppFlow         25         25      0.993          1      0.995      0.919
               Appsync          6          6      0.969          1      0.995      0.722
                Athena         36         37      0.995          1      0.995      0.928
                Aurora         44         54      0.998          1      0.995      0.936
          Auto Scaling         48         73          1      0.998      0.995      0.837
    Auto Scaling Group          4         10      0.992          1      0.995      0.783
       Automated Tests         15         20      0.991          1      0.995      0.931
     Availability Zone         12         24      0.994          1      0.995       0.87
                Backup          3          6      0.972          1      0.995      0.931
     Build Environment          7          7      0.972          1      0.995      0.858
                   CDN          5          5      0.965          1      0.995      0.877
                   CUR          5          5      0.965          1      0.995      0.705
          Call Metrics         25         25      0.993          1      0.995      0.881
       Call Recordings         25         25      0.994          1      0.995      0.831
   Certificate Manager         43         43      0.996          1      0.995      0.938
                Client          3         13      0.856      0.923      0.938      0.832
       Cloud Connector         11         22      0.993          1      0.995      0.915
             Cloud Map          5          5      0.969          1      0.995      0.957
          Cloud Search         19         19      0.977          1      0.995      0.925
           Cloud Trail         53         53      0.977      0.981      0.982      0.946
           Cloud Watch        113        135      0.993      0.994      0.994      0.903
  CloudFormation Stack         32         37      0.995          1      0.995      0.951
              CloudHSM         30         30      0.994          1      0.995      0.935
      CloudWatch Alarm         18         23      0.995          1      0.995      0.908
            Cloudfront        102        108      0.994          1      0.995      0.911
             CodeBuild         30         50      0.995          1      0.995      0.943
            CodeCommit         17         17      0.991          1      0.995      0.981
            CodeDeploy          5          5      0.968          1      0.995      0.963
          CodePipeline         43         43      0.996          1      0.995      0.883
               Cognito         90        104      0.977      0.962      0.955      0.894
            Comprehend         25         25      0.992          1      0.995      0.971
                Config         38        163      0.987          1      0.983      0.824
               Connect         25         25      0.993          1      0.995      0.975
  Connect Contact Lens         25         25      0.958          1      0.995      0.874
             Container         17         66          1      0.996      0.995      0.852
         Control Tower          5          5       0.97          1      0.995      0.915
      Customer Gateway          8         11      0.986          1      0.995      0.884
                   DSI          5         10      0.982          1      0.995      0.836
         Data Pipeline          5          5          1      0.842      0.995      0.976
              DataSync          5          5      0.963          1      0.995       0.95
          Deploy Stage         10         10      0.985          1      0.995      0.832
             Detective         25         25      0.992          1      0.995      0.984
        Direct Connect         21         21      0.991          1      0.995      0.944
          Distribution          5          5          1      0.672      0.995      0.972
          Docker Image         21         72      0.984      0.864      0.992      0.783
             Dynamo DB        169        263          1          1      0.995       0.92
                   EBS         27         37      0.998          1      0.995      0.901
                   EC2        179        418      0.994      0.957      0.994       0.86
                   EFS         22         30      0.961      0.967      0.985      0.906
      EFS Mount Target         52        102      0.971      0.975      0.987      0.803
                   EKS         53         59      0.958      0.983      0.993      0.956
                   ELB        111        150      0.998      0.933      0.949      0.892
                   EMR         10         10      0.982          1      0.995      0.936
         Edge Location          5          7      0.982          1      0.995      0.946
           ElastiCache         22         26          1       0.99      0.995      0.924
Elastic Container Registry         43         43      0.996          1      0.995      0.958
Elastic Container Service         50         60      0.977      0.983      0.994       0.85
        Elastic Search         38         38      0.994          1      0.995      0.864
Elemental MediaConvert         16         18      0.929          1      0.992      0.954
Elemental MediaPackage          5          5          1      0.822      0.995      0.995
                 Email          5          5      0.967          1      0.995        0.9
              Endpoint          5          5      0.969          1      0.995      0.916
             Event Bus          5          5      0.966          1      0.995      0.995
           EventBridge         35        135      0.999          1      0.995      0.866
   Experiment Duration          7          7          1          0      0.906      0.706
           Experiments          7          7          1          0      0.871      0.851
               Fargate         29         71      0.997          1      0.995      0.896
Fault Injection Simulator         15         15      0.994          1      0.995      0.907
      Firewall Manager         25         25      0.992          1      0.995      0.871
                 Flask          8         24          1      0.977      0.995      0.724
             Flow logs         25        100      0.983       0.99      0.995      0.693
              GameLift          5          5      0.967          1      0.995      0.917
                   Git          8          8      0.955          1      0.995      0.906
                Github         17         18      0.993          1      0.995      0.951
               Glacier         10         10      0.982          1      0.995      0.968
                  Glue         19         38      0.996          1      0.995      0.934
         Glue DataBrew          7          7      0.973          1      0.995      0.995
               Grafana         10         10       0.98          1      0.995      0.995
             GuardDuty         34        134      0.998          1      0.995       0.84
                   IAM         66        207      0.984      0.971      0.994      0.854
              IAM Role         41        169      0.978      0.941      0.982      0.761
              IOT Core         13         17      0.989          1      0.995      0.956
                 Image         11         11      0.987          1      0.995      0.845
         Image Builder          5          5      0.964          1      0.995      0.995
               Ingress          5          5      0.967          1      0.995      0.995
       Inspector Agent         25         25      0.994          1      0.995      0.978
             Instances          3          6      0.483      0.333       0.68      0.616
              Internet         59         82       0.91      0.991      0.989      0.903
      Internet Gateway         51         87      0.963      0.954      0.992      0.835
               Jenkins          3          6      0.974          1      0.995      0.884
Key Management Service         47         75      0.997          1      0.995      0.851
                Kibana          7          7      0.978          1      0.995      0.955
  Kinesis Data Streams         72         85      0.988       0.99      0.984      0.916
            Kubernetes          8          8      0.981          1      0.995      0.893
                Lambda        255        675      0.997      0.997      0.995      0.929
                   Lex          5          5      0.965          1      0.995      0.995
                    MQ          6         12      0.988          1      0.995      0.808
      Machine Learning          9          9       0.92          1      0.995      0.908
                 Macie         45        110      0.999          1      0.995      0.821
           Marketplace          5          5      0.987          1      0.995      0.819
             Memcached          5         10       0.98          1      0.995      0.915
         Mobile Client         36         41          1      0.943      0.995       0.85
              Mongo DB         11         23      0.971          1      0.995      0.729
                 MySQL          7          7      0.984          1      0.995      0.832
           NAT Gateway         44         85      0.986          1      0.992      0.929
               Neptune          5          5      0.967          1      0.995      0.504
       Network Adapter          5          5      0.965          1      0.995      0.933
      Network Firewall         25         25      0.993          1      0.995      0.922
              Notebook          5          5      0.977          1      0.995      0.924
      Order Controller          5          5      0.931          1      0.995      0.828
    Organization Trail         30        105      0.999          1      0.995      0.868
       Parameter Store          7          7      0.981          1      0.995      0.937
              Pinpoint          5          5      0.962          1      0.995      0.971
            PostgreSQL          7          7      0.978          1      0.995      0.912
          Private Link         25         25      0.993          1      0.995      0.939
        Private Subnet        106        263      0.878      0.962      0.959      0.782
            Prometheus         10         10      0.981          1      0.995      0.995
         Public Subnet        104        216      0.995       0.95      0.994      0.802
               Quarkus         10         10       0.98          1      0.995      0.939
            Quicksight         32         34      0.995          1      0.995      0.876
                   RDS         93        197          1      0.993      0.995      0.896
                 React          3          3      0.991          1      0.995      0.741
                 Redis         10         21      0.993          1      0.995      0.911
              Redshift         45         46      0.995      0.978      0.981      0.891
                Region         36         53      0.998          1      0.995      0.808
           Rekognition         14         14      0.986          1      0.995      0.963
               Results          7          7          1          0      0.871      0.711
              Route 53         40         40      0.995          1      0.995       0.93
               Route53         87        138      0.985          1      0.992      0.908
                    S3        260        514      0.996      0.994      0.993      0.899
                   SAR          5          5      0.964          1      0.995      0.995
                   SDK         26         88          1      0.949      0.995      0.866
                   SES         14         17      0.988          1      0.995      0.892
                   SNS         62         69      0.993      0.957      0.987      0.934
                   SQS         43         44      0.996          1      0.995      0.925
             SSM Agent         25         25      0.992          1      0.995      0.941
             Sagemaker         18         61          1      0.572      0.995      0.755
        Secret Manager         30         30      0.991          1      0.995      0.892
        Security Group          5          5      0.965          1      0.995      0.995
          Security Hub         30        130      0.998          1      0.995       0.83
                Server         27         42      0.997          1      0.995      0.878
       Service Catalog          8         23      0.993          1      0.995       0.91
                Shield         31         31      0.994          1      0.995      0.922
               Sign-On         25         25      0.992          1      0.995      0.995
                 Slack         12         12      0.978          1      0.995      0.922
              Snowball         10         10      0.985          1      0.995      0.972
                 Stack          5          5      0.968          1      0.995      0.957
         Step Function          7         21      0.953          1      0.995      0.945
       Storage Gateway         10         10      0.982          1      0.995      0.995
            SwaggerHub          3          3      0.949          1      0.995      0.964
       Systems Manager         39         64      0.997          1      0.995      0.964
                    TV          5          5      0.965          1      0.995      0.872
                 Table         20         40       0.99          1      0.995      0.875
           Task Runner          5          5      0.972          1      0.995      0.976
             Terraform         13         13      0.988          1      0.995      0.905
             Text File         14         32          1      0.952      0.995      0.885
              Textract          3          3      0.941          1      0.995      0.995
            Transcribe          9          9      0.979          1      0.995      0.951
       Transfer Family         16         16      0.989          1      0.995      0.975
       Transit Gateway         10         10      0.983          1      0.995       0.92
             Translate         19         19      0.991          1      0.995      0.932
       Trusted Advisor          5          5      0.979          1      0.995      0.941
                Twilio          7          7      0.975          1      0.995      0.962
                 Users        152        204      0.995      0.991      0.995      0.874
                   VDA         11         11      0.986          1      0.995      0.961
            VP Gateway          6          7       0.96          1      0.995      0.837
            VPC Router          9         16       0.99          1      0.995      0.875
        VPN Connection          5          8      0.982          1      0.995      0.914
                   WAF         43         46          1      0.934      0.995      0.959
           Web Clients         45         62          1      0.722       0.98      0.846
              Websites          5          5      0.981          1      0.995       0.86
                 X-Ray         16         20      0.986          1      0.995      0.935
                   aws        240        322      0.992      0.981      0.995      0.855
          cache Worker          8          8      0.979          1      0.995      0.929
Speed: 0.2ms preprocess, 8.8ms inference, 0.0ms loss, 1.5ms postprocess per image
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100
🚀 Save dir: C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100
✅ best.pt:  C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_100\weights\best.pt
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11n summary (fused): 100 layers, 2,672,434 parameters, 0 gradients, 6.8 GFLOPs
val: Fast image access  (ping: 0.00.0 ms, read: 231.0122.0 MB/s, size: 343.9 KB)
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels... 386 images, 0 backgrounds, 0 corrupt: 100%|██████████| 
val: New cache created: C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels.cache
█████████████████████████████████ 100% | 5.39/5.39 MB [00:04<00:00,  1.26MB/s]: 
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 49/49 [00:03<00:00, 13.35it/s]
                   all        386       7672      0.977      0.954      0.983      0.923
                   ACM         22         22      0.992          1      0.995      0.986
                   ALB         58         74      0.993      0.905       0.99      0.892: 100%|██████████| 49/49 [00:03<00:00, 11.23it/s]
                   AMI          8         13      0.984          1      0.995       0.97
           API-Gateway        201        304      0.997      0.993      0.994      0.951
Active Directory Service         15         15      0.986          1      0.995      0.995
              Airflow_          3          6      0.959          1      0.995      0.913
               Amplify         18         18      0.993          1      0.995      0.942
    Analytics Services          5          5      0.967          1      0.995      0.895
               AppFlow         12         12      0.983          1      0.995      0.971
               Appsync          8          8      0.975          1      0.995      0.906
                Athena         32         33      0.993          1      0.995      0.984
                Aurora         27         36      0.996      0.889      0.925       0.89
          Auto Scaling         45         75          1      0.946      0.988      0.831
    Auto Scaling Group          3          8      0.986          1      0.995      0.799
       Automated Tests         12         17      0.989          1      0.995      0.944
     Availability Zone         10         20      0.992          1      0.995      0.928
                Backup          3          6      0.967          1      0.995      0.954
     Build Environment          6          6      0.972          1      0.995      0.829
                   CDN          7          7       0.97          1      0.995      0.942
                   CUR          6          6      0.966          1      0.995       0.96
          Call Metrics         12         12      0.989          1      0.995      0.909
       Call Recordings         12         12      0.994          1      0.995      0.877
   Certificate Manager         28         28      0.994          1      0.995      0.983
                Client          3          8      0.635       0.87      0.765      0.664
       Cloud Connector          7         14      0.988          1      0.995      0.921
             Cloud Map          5          5      0.978          1      0.995      0.995
          Cloud Search         14         14      0.984          1      0.995      0.985
           Cloud Trail         39         41      0.992      0.976       0.98      0.959
           Cloud Watch        126        151      0.999          1      0.995      0.911
  CloudFormation Stack         38         45      0.995          1      0.995      0.961
              CloudHSM         13         13      0.985          1      0.995      0.989
      CloudWatch Alarm         18         23      0.993          1      0.995      0.914
            Cloudfront         97        101      0.986          1      0.995      0.942
             CodeBuild         33         53      0.997          1      0.995      0.952
            CodeCommit         15         15      0.989          1      0.995      0.985
            CodeDeploy          5          5      0.967          1      0.995      0.971
          CodePipeline         43         43      0.973          1      0.972      0.939
               Cognito         85        100      0.997       0.98      0.982      0.963
            Comprehend         27         27      0.994          1      0.995      0.992
                Config         25         65      0.968          1      0.967       0.95
               Connect         12         12      0.983          1      0.995      0.987
  Connect Contact Lens         12         12       0.99          1      0.995       0.91
             Container         18         81      0.999          1      0.995      0.869
         Control Tower          7          7      0.993          1      0.995      0.995
      Customer Gateway          5         11       0.96          1      0.995      0.927
                   DSI          5         10      0.981          1      0.995      0.849
         Data Pipeline          5          5          1      0.847      0.995      0.948
              DataSync          5          5      0.962          1      0.995      0.971
          Deploy Stage          7          7      0.975          1      0.995      0.803
             Detective          8          8      0.975          1      0.995      0.975
        Direct Connect         19         26      0.992      0.962       0.97      0.846
          Distribution          5          5          1      0.675      0.962      0.962
          Docker Image         18         61          1      0.806      0.969      0.818
             Dynamo DB        174        270      0.999       0.97      0.986       0.94
                   EBS         24         36      0.998          1      0.995      0.915
                   EC2        166        406      0.987      0.939      0.987      0.874
                   EFS         28         36       0.94      0.864      0.935      0.875
      EFS Mount Target         35         54       0.98      0.909      0.936      0.868
                   EKS         51         58      0.996      0.983      0.995      0.956
                   ELB        104        149      0.997       0.94      0.965      0.901
                   EMR          5          5      0.963          1      0.995      0.995
         Edge Location          3          5      0.967          1      0.995      0.827
           ElastiCache         25         31          1      0.871      0.944      0.884
Elastic Container Registry         51         51      0.998          1      0.995      0.987
Elastic Container Service         50         62      0.996      0.952      0.994      0.877
        Elastic Search         32         33      0.995          1      0.995      0.923
Elemental MediaConvert         17         20      0.832          1       0.97      0.967
Elemental MediaPackage          5          5          1      0.251       0.84       0.84
                 Email          5          5          1      0.845      0.995      0.858
              Endpoint          6          6      0.963          1      0.995       0.93
             Event Bus          5          5      0.961          1      0.995      0.995
           EventBridge         21         53      0.996          1      0.995      0.975
   Experiment Duration          5          5          1          0      0.851      0.701
           Experiments          5          5          1          0      0.817      0.817
               Fargate         30         72      0.997          1      0.995       0.94
Fault Injection Simulator         12         12      0.988          1      0.995      0.903
      Firewall Manager          8          8       0.98          1      0.995      0.984
                 Flask          6         18      0.997          1      0.995      0.793
             Flow logs          8         32      0.997          1      0.995      0.892
              GameLift          5          5      0.924          1      0.995       0.92
                   Git          6          6      0.972          1      0.995      0.975
                Github         20         25      0.994          1      0.995      0.928
               Glacier          5          5       0.96          1      0.995      0.995
                  Glue         15         30      0.996          1      0.995      0.917
         Glue DataBrew          7          7      0.971          1      0.995      0.995
               Grafana          8          8      0.975          1      0.995      0.995
             GuardDuty         17         49      0.996          1      0.995      0.954
                   IAM         51        104      0.997      0.933       0.99      0.893
              IAM Role         25         68      0.969      0.935      0.967      0.826
              IOT Core         12         14          1      0.962      0.995      0.975
                 Image         13         13       0.99          1      0.995      0.949
         Image Builder          5          5      0.959          1      0.995      0.995
               Ingress          5          5      0.969          1      0.995      0.995
       Inspector Agent          8          8      0.977          1      0.995      0.995
             Instances          3          6      0.512      0.353      0.663      0.597
              Internet         63         86      0.933       0.97      0.985      0.909
      Internet Gateway         32         50      0.961      0.986      0.994      0.901
               Jenkins          3          6      0.999          1      0.995      0.947
Key Management Service         29         40          1      0.981      0.995      0.988
                Kibana          7          7      0.976          1      0.995      0.921
  Kinesis Data Streams         50         66      0.969       0.94      0.977      0.945
            Kubernetes          6          6      0.967          1      0.995      0.924
                Lambda        243        673      0.999      0.997      0.995      0.957
                   Lex          5          5      0.961          1      0.995      0.995
                    MQ          5         11      0.996          1      0.995       0.85
      Machine Learning         11         11      0.918      0.727      0.965      0.923
                 Macie         27         70      0.997          1      0.995      0.928
           Marketplace          5          5      0.985          1      0.995      0.637
             Memcached          6         12      0.983          1      0.995      0.909
         Mobile Client         40         49          1      0.876      0.993      0.853
              Mongo DB          9         21          1          1      0.995      0.811
                 MySQL          7          7      0.989          1      0.995      0.899
           NAT Gateway         46         88      0.966      0.955       0.96       0.92
               Neptune          6          6      0.972          1      0.995      0.901
       Network Adapter          5          5       0.96          1      0.995      0.995
      Network Firewall          8          8      0.977          1      0.995      0.976
              Notebook          5          5      0.977          1      0.995      0.953
      Order Controller          5          5       0.95          1      0.995      0.895
    Organization Trail         17         41      0.996          1      0.995      0.955
       Parameter Store          7          7      0.976          1      0.995      0.974
              Pinpoint          5          5      0.958          1      0.995      0.995
            PostgreSQL          7          7      0.975          1      0.995      0.942
          Private Link         24         24      0.992          1      0.995      0.955
        Private Subnet         89        208      0.985      0.952      0.973      0.831
            Prometheus          8          8      0.976          1      0.995      0.995
         Public Subnet         90        203      0.995      0.922      0.978       0.81
               Quarkus          8          8      0.975          1      0.995      0.995
            Quicksight         19         21      0.991          1      0.995      0.972
                   RDS         83        163      0.955      0.902      0.948      0.868
                 React          4          4      0.955          1      0.995      0.872
                 Redis         10         25      0.979       0.96      0.993      0.948
              Redshift         27         29      0.994      0.966       0.97      0.937
                Region         36         52          1      0.981      0.995      0.834
           Rekognition         14         14      0.985          1      0.995      0.977
               Results          5          5          1          0       0.83      0.812
              Route 53         21         21      0.946          1      0.969      0.964
               Route53         98        167      0.987      0.994      0.987      0.925
                    S3        256        520      0.998      0.994      0.995       0.93
                   SAR          5          5      0.959          1      0.995      0.995
                   SDK         24         80      0.987      0.983      0.983      0.884
                   SES         17         20          1      0.958      0.995      0.917
                   SNS         63         69          1      0.975      0.995      0.958
                   SQS         49         50      0.999          1      0.995      0.955
             SSM Agent          8          8      0.973          1      0.995      0.995
             Sagemaker         16         59          1      0.538      0.994      0.757
        Secret Manager         14         14      0.989          1      0.995      0.973
        Security Group          5          5       0.96          1      0.995      0.943
          Security Hub         13         45      0.996          1      0.995      0.967
                Server         20         32      0.995          1      0.995       0.88
       Service Catalog         10         31      0.994          1      0.995      0.909
                Shield         15         15      0.986          1      0.995       0.99
               Sign-On          8          8      0.974          1      0.995      0.995
                 Slack         13         13      0.985          1      0.995      0.979
              Snowball          5          5      0.963          1      0.995      0.995
                 Stack          5          5      0.986          1      0.995      0.926
         Step Function          8         24      0.993          1      0.995      0.925
       Storage Gateway          5          5      0.964          1      0.995      0.995
            SwaggerHub          5          5      0.968          1      0.995      0.958
       Systems Manager         20         28      0.993          1      0.995      0.969
                    TV          6          6          1       0.97      0.995      0.865
                 Table         23         46      0.987          1      0.995       0.92
           Task Runner          5          5      0.966          1      0.995      0.995
             Terraform         11         11      0.985          1      0.995      0.898
             Text File         11         28      0.861      0.964      0.947      0.864
              Textract          5          5      0.958          1      0.995      0.995
            Transcribe          9          9      0.977          1      0.995      0.995
       Transfer Family         15         15      0.988          1      0.995      0.978
       Transit Gateway         12         12      0.984          1      0.995      0.968
             Translate         19         19      0.989          1      0.995      0.995
       Trusted Advisor          6          6       0.98          1      0.995      0.966
                Twilio          7          7       0.97          1      0.995      0.995
                 Users        144        196          1      0.972      0.994      0.906
                   VDA          7          7      0.977          1      0.995      0.917
            VP Gateway          5          6      0.974      0.833      0.843      0.742
            VPC Router          8         16      0.989          1      0.995      0.851
        VPN Connection          3          9      0.995          1      0.995      0.871
                   WAF         25         28      0.986          1      0.995      0.947
           Web Clients         50         62      0.995      0.774       0.98      0.861
              Websites          9          9      0.985          1      0.995      0.934
                 X-Ray         19         21      0.985          1      0.995      0.945
                   aws        243        326      0.984      0.972      0.991      0.881
          cache Worker          7          7      0.971          1      0.995      0.938
Speed: 0.2ms preprocess, 4.9ms inference, 0.0ms loss, 0.9ms postprocess per image
Saving C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val\predictions.json...
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val

🎯 Test Metrics (mean per class):
  Precision:    0.977
  Recall:       0.954
  mAP@0.5:      0.983
  mAP@0.5:0.95: 0.923

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_02.png: 576x640 2 Cloud Watchs, 4 EC2s, 2 NAT Gateways, 3 Private Subnets, 3 Public Subnets, 1 RDS, 1 Region, 1 Route53, 2 S3s, 1 Users, 2 WAFs, 1 aws, 62.1ms
Speed: 3.4ms preprocess, 62.1ms inference, 3.8ms postprocess per image at shape (1, 3, 576, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict2
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict2\labels
✅ Detailed JSON saved to data\reports\yolo11n_custom_100\results.json
✅ Summary JSON saved to data\reports\yolo11n_custom_100\report.json
[ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
names: {0: 'ACM', 1: 'ALB', 2: 'AMI', 3: 'API-Gateway', 4: 'Active Directory Service', 5: 'Airflow_', 6: 'Amplify', 7: 'Analytics Services', 8: 'AppFlow', 9: 'Ap
psync', 10: 'Athena', 11: 'Aurora', 12: 'Auto Scaling', 13: 'Auto Scaling Group', 14: 'Automated Tests', 15: 'Availability Zone', 16: 'Backup', 17: 'Build Enviro
nment', 18: 'CDN', 19: 'CUR', 20: 'Call Metrics', 21: 'Call Recordings', 22: 'Certificate Manager', 23: 'Client', 24: 'Cloud Connector', 25: 'Cloud Map', 26: 'Cl
oud Search', 27: 'Cloud Trail', 28: 'Cloud Watch', 29: 'CloudFormation Stack', 30: 'CloudHSM', 31: 'CloudWatch Alarm', 32: 'Cloudfront', 33: 'CodeBuild', 34: 'Co
deCommit', 35: 'CodeDeploy', 36: 'CodePipeline', 37: 'Cognito', 38: 'Comprehend', 39: 'Config', 40: 'Connect', 41: 'Connect Contact Lens', 42: 'Container', 43: '
Control Tower', 44: 'Customer Gateway', 45: 'DSI', 46: 'Data Pipeline', 47: 'DataSync', 48: 'Deploy Stage', 49: 'Detective', 50: 'Direct Connect', 51: 'Distribut
ion', 52: 'Docker Image', 53: 'Dynamo DB', 54: 'EBS', 55: 'EC2', 56: 'EFS', 57: 'EFS Mount Target', 58: 'EKS', 59: 'ELB', 60: 'EMR', 61: 'Edge Location', 62: 'El
astiCache', 63: 'Elastic Container Registry', 64: 'Elastic Container Service', 65: 'Elastic Search', 66: 'Elemental MediaConvert', 67: 'Elemental MediaPackage', 
68: 'Email', 69: 'Endpoint', 70: 'Event Bus', 71: 'EventBridge', 72: 'Experiment Duration', 73: 'Experiments', 74: 'Fargate', 75: 'Fault Injection Simulator', 76
: 'Firewall Manager', 77: 'Flask', 78: 'Flow logs', 79: 'GameLift', 80: 'Git', 81: 'Github', 82: 'Glacier', 83: 'Glue', 84: 'Glue DataBrew', 85: 'Grafana', 86: '
GuardDuty', 87: 'IAM', 88: 'IAM Role', 89: 'IOT Core', 90: 'Image', 91: 'Image Builder', 92: 'Ingress', 93: 'Inspector Agent', 94: 'Instances', 95: 'Internet', 9
6: 'Internet Gateway', 97: 'Jenkins', 98: 'Key Management Service', 99: 'Kibana', 100: 'Kinesis Data Streams', 101: 'Kubernetes', 102: 'Lambda', 103: 'Lex', 104:
 'MQ', 105: 'Machine Learning', 106: 'Macie', 107: 'Marketplace', 108: 'Memcached', 109: 'Mobile Client', 110: 'Mongo DB', 111: 'MySQL', 112: 'NAT Gateway', 113:
 'Neptune', 114: 'Network Adapter', 115: 'Network Firewall', 116: 'Notebook', 117: 'Order Controller', 118: 'Organization Trail', 119: 'Parameter Store', 120: 'P
inpoint', 121: 'PostgreSQL', 122: 'Private Link', 123: 'Private Subnet', 124: 'Prometheus', 125: 'Public Subnet', 126: 'Quarkus', 127: 'Quicksight', 128: 'RDS', 
129: 'React', 130: 'Redis', 131: 'Redshift', 132: 'Region', 133: 'Rekognition', 134: 'Results', 135: 'Route 53', 136: 'Route53', 137: 'S3', 138: 'SAR', 139: 'SDK
', 140: 'SES', 141: 'SNS', 142: 'SQS', 143: 'SSM Agent', 144: 'Sagemaker', 145: 'Secret Manager', 146: 'Security Group', 147: 'Security Hub', 148: 'Server', 149:
 'Service Catalog', 150: 'Shield', 151: 'Sign-On', 152: 'Slack', 153: 'Snowball', 154: 'Stack', 155: 'Step Function', 156: 'Storage Gateway', 157: 'SwaggerHub', 
158: 'Systems Manager', 159: 'TV', 160: 'Table', 161: 'Task Runner', 162: 'Terraform', 163: 'Text File', 164: 'Textract', 165: 'Transcribe', 166: 'Transfer Famil
y', 167: 'Transit Gateway', 168: 'Translate', 169: 'Trusted Advisor', 170: 'Twilio', 171: 'Users', 172: 'VDA', 173: 'VP Gateway', 174: 'VPC Router', 175: 'VPN Connection', 176: 'WAF', 177: 'Web Clients', 178: 'Websites', 179: 'X-Ray', 180: 'aws', 181: 'cache Worker'}
obb: None
orig_img: array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)
orig_shape: (993, 1167)
path: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_02.png'
probs: None
save_dir: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\runs\\detect\\predict2'
speed: {'preprocess': 3.3930000208783895, 'inference': 62.051799992332235, 'postprocess': 3.7826000188943}]
████████████████████████████████ 100% | 0.46/0.46 MB [05:04<00:00, 662.77s/MB]: 
████████████████████████████████ 100% | 0.44/0.44 MB [05:04<00:00, 692.89s/MB]:
████████████████████████████████ 100% | 0.43/0.43 MB [05:04<00:00, 709.01s/MB]:
```

Report:
```bash
C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\.venv\Scripts\python.exe C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\report.py 

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_01.jpg: 544x640 3 Cloud Watchs, 1 Dynamo DB, 5 Lambdas, 1 S3, 2 SNSs, 2 Userss, 41.6ms
Speed: 2.2ms preprocess, 41.6ms inference, 86.1ms postprocess per image at shape (1, 3, 544, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict7
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict7\labels
✅ Detailed JSON saved to data\reports\yolo11n_custom_200\results.json
✅ Summary JSON saved to data\reports\yolo11n_custom_200\report.json
Reports generated: data/reports/yolo11n_custom_200
```

yolo11s

```bash
C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\.venv\Scripts\python.exe C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\model.py 
New https://pypi.org/project/ultralytics/8.3.162 available  Update with 'pip install -U ultralytics'
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
engine\trainer: agnostic_nms=False, amp=True, augment=True, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data/dataset/aws/data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.001, lrf=0.05, mask_ratio=4, max_det=300, mixup=0.5, mode=train, model=./data/model/yolo11s.pt, momentum=0.937, mosaic=1.0, multi_scale=True, name=yolo11s_custom_100, nbs=64, nms=False, opset=None, optimize=False, optimizer=AdamW, overlap_mask=True, patience=10, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, save=True, save_conf=False, save_crop=False, save_dir=C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Overriding model.yaml nc=80 with nc=182

                   from  n    params  module                                       arguments                     
  0                  -1  1       928  ultralytics.nn.modules.conv.Conv             [3, 32, 3, 2]                 
  1                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  2                  -1  1     26080  ultralytics.nn.modules.block.C3k2            [64, 128, 1, False, 0.25]     
  3                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
  4                  -1  1    103360  ultralytics.nn.modules.block.C3k2            [128, 256, 1, False, 0.25]    
  5                  -1  1    590336  ultralytics.nn.modules.conv.Conv             [256, 256, 3, 2]              
  6                  -1  1    346112  ultralytics.nn.modules.block.C3k2            [256, 256, 1, True]           
  7                  -1  1   1180672  ultralytics.nn.modules.conv.Conv             [256, 512, 3, 2]              
  8                  -1  1   1380352  ultralytics.nn.modules.block.C3k2            [512, 512, 1, True]           
  9                  -1  1    656896  ultralytics.nn.modules.block.SPPF            [512, 512, 5]                 
 10                  -1  1    990976  ultralytics.nn.modules.block.C2PSA           [512, 512, 1]                 
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 13                  -1  1    443776  ultralytics.nn.modules.block.C3k2            [768, 256, 1, False]          
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 16                  -1  1    127680  ultralytics.nn.modules.block.C3k2            [512, 128, 1, False]          
 17                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 19                  -1  1    345472  ultralytics.nn.modules.block.C3k2            [384, 256, 1, False]          
 20                  -1  1    590336  ultralytics.nn.modules.conv.Conv             [256, 256, 3, 2]              
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 22                  -1  1   1511424  ultralytics.nn.modules.block.C3k2            [768, 512, 1, True]           
 23        [16, 19, 22]  1    889842  ultralytics.nn.modules.head.Detect           [182, [128, 256, 512]]        
YOLO11s summary: 181 layers, 9,498,226 parameters, 9,498,210 gradients, 21.9 GFLOPs

Transferred 493/499 items from pretrained weights
ClearML Task: created new task id=994706fd3f00409bbf46569051a5000f
ClearML results page: https://app.clear.ml/projects/14f0119248fa451f826c387955b212a3/experiments/994706fd3f00409bbf46569051a5000f/output/log
WARNING ClearML Initialized a new task. If you want to run remotely, please add clearml-init and connect your arguments before initializing YOLO.
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
AMP: checks passed 
train: Fast image access  (ping: 0.00.0 ms, read: 203.2142.6 MB/s, size: 416.9 KB)
train: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\train\labels.cache... 5276 images, 0 backgrounds, 0 corrupt: 100%|██████████| 5276/5276 [00:00<?, ?it/s]
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))
val: Fast image access  (ping: 0.00.0 ms, read: 214.5119.4 MB/s, size: 226.2 KB)
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\labels.cache... 393 images, 0 backgrounds, 0 corrupt: 100%|██████████| 393/393 [00:00<?, ?it/s]
Plotting labels to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100\labels.jpg... 
optimizer: AdamW(lr=0.001, momentum=0.937) with parameter groups 81 weight(decay=0.0), 88 weight(decay=0.0005), 87 bias(decay=0.0)
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100
Starting training for 100 epochs...
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      1/100      7.43G      1.172      2.474     0.9557        147        352: 100%|██████████| 660/660 [01:58<00:00,  5.58it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:03<00:00,  6.84it/s]
                   all        393       9029       0.59      0.331      0.375       0.27

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      2/100       6.4G      1.073      1.648     0.9296        505        704:  15%|█▌        | 99/660 [00:15<01:17,  7.20it/s]ClearML Monitor: Could not detect iteration reporting, falling back to iterations as seconds-from-start
      2/100      6.91G      1.051       1.57      0.927        320        640:  44%|████▍     | 292/660 [00:45<00:57,  6.35it/s]ClearML Monitor: Reporting detected, reverting back to iteration based reporting
      2/100      6.91G      1.025      1.443     0.9223        249        544: 100%|██████████| 660/660 [01:43<00:00,  6.40it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.54it/s]
                   all        393       9029      0.719      0.656      0.744       0.57
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      3/100      6.03G      0.991      1.171     0.9111        299        416: 100%|██████████| 660/660 [01:40<00:00,  6.58it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.06it/s]
                   all        393       9029      0.755      0.799      0.862      0.671
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      4/100      6.93G     0.9356     0.9777     0.9004        289        736: 100%|██████████| 660/660 [01:42<00:00,  6.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.86it/s]
                   all        393       9029       0.87      0.855      0.927      0.749

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      5/100      8.45G     0.8959     0.8651     0.8877        179        672: 100%|██████████| 660/660 [01:41<00:00,  6.48it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.39it/s]
                   all        393       9029      0.868      0.922      0.963      0.782

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      6/100      7.55G     0.8699      0.801     0.8823        201        704: 100%|██████████| 660/660 [01:42<00:00,  6.41it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.51it/s]
                   all        393       9029      0.884      0.916       0.96      0.788

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      7/100      7.82G     0.8397     0.7485       0.88        169        512: 100%|██████████| 660/660 [01:53<00:00,  5.84it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.48it/s]
                   all        393       9029      0.901       0.93      0.961      0.806
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      8/100      7.76G     0.8197     0.7074     0.8721        127        960: 100%|██████████| 660/660 [01:43<00:00,  6.37it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.80it/s]
                   all        393       9029      0.939      0.947      0.978      0.835
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      9/100      6.31G     0.8042     0.6743     0.8678        188        960: 100%|██████████| 660/660 [01:42<00:00,  6.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.08it/s]
                   all        393       9029      0.921      0.961       0.98      0.827

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     10/100      7.04G     0.7823     0.6316     0.8643        152        352: 100%|██████████| 660/660 [01:43<00:00,  6.40it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.38it/s]
                   all        393       9029      0.948       0.97      0.985      0.847
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     11/100      7.59G     0.7675      0.629     0.8619        302        960: 100%|██████████| 660/660 [01:46<00:00,  6.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.25it/s]
                   all        393       9029      0.953      0.966      0.987      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     12/100      7.14G     0.7485     0.5976      0.854        208        576: 100%|██████████| 660/660 [01:40<00:00,  6.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.90it/s]
                   all        393       9029      0.952      0.959      0.983       0.85
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     13/100      6.94G     0.7346      0.585     0.8522        131        576: 100%|██████████| 660/660 [01:43<00:00,  6.40it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.90it/s]
                   all        393       9029      0.934      0.974      0.983      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     14/100       7.2G     0.7318     0.5792     0.8506        182        864: 100%|██████████| 660/660 [01:39<00:00,  6.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.05it/s]
                   all        393       9029      0.937      0.985      0.986      0.863

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     15/100      8.23G     0.7084     0.5481     0.8485        149        864: 100%|██████████| 660/660 [01:53<00:00,  5.80it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.58it/s]
                   all        393       9029      0.948      0.978      0.989      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     16/100       7.2G     0.7074     0.5415     0.8431        197        544: 100%|██████████| 660/660 [01:37<00:00,  6.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.27it/s]
                   all        393       9029      0.941      0.977      0.989      0.873
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     17/100      7.91G     0.7007     0.5506     0.8451        216        832: 100%|██████████| 660/660 [02:33<00:00,  4.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.40it/s]
                   all        393       9029      0.959      0.964      0.989      0.883

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     18/100      6.82G      0.684     0.5261     0.8443         76        672: 100%|██████████| 660/660 [01:44<00:00,  6.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.25it/s]
                   all        393       9029      0.954       0.97      0.988      0.883
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     19/100      7.21G     0.6775     0.5169       0.84        175        896: 100%|██████████| 660/660 [01:40<00:00,  6.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.92it/s]
                   all        393       9029      0.953      0.984      0.989       0.88
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     20/100      9.42G     0.6683     0.5078     0.8383        203        928: 100%|██████████| 660/660 [01:48<00:00,  6.07it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.44it/s]
                   all        393       9029      0.947      0.986      0.991      0.891

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     21/100      6.76G     0.6594     0.4994     0.8364        142        736: 100%|██████████| 660/660 [01:41<00:00,  6.49it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.17it/s]
                   all        393       9029      0.953      0.983      0.989      0.887
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     22/100      6.57G     0.6536     0.4927     0.8356        186        640: 100%|██████████| 660/660 [01:42<00:00,  6.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.19it/s]
                   all        393       9029      0.958      0.971      0.989      0.898

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     23/100       8.7G     0.6418     0.4781     0.8337        235        896: 100%|██████████| 660/660 [01:49<00:00,  6.02it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:03<00:00,  7.62it/s]
                   all        393       9029      0.969      0.966       0.99      0.899
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     24/100      8.11G     0.6363     0.4707     0.8318        281        416: 100%|██████████| 660/660 [01:45<00:00,  6.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:03<00:00,  8.33it/s]
                   all        393       9029      0.961      0.978       0.99      0.906

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     25/100      6.98G     0.6356     0.4757     0.8311        166        896: 100%|██████████| 660/660 [01:42<00:00,  6.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.56it/s]
                   all        393       9029      0.963      0.969      0.988      0.888
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     26/100      8.32G     0.6263     0.4687     0.8288        231        960: 100%|██████████| 660/660 [01:48<00:00,  6.07it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.62it/s]
                   all        393       9029      0.972      0.975       0.99      0.902
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     27/100      6.88G     0.6232     0.4609     0.8281        221        448: 100%|██████████| 660/660 [01:39<00:00,  6.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.42it/s]
                   all        393       9029      0.961      0.976       0.99      0.899

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     28/100      8.26G     0.6145     0.4533      0.827        366        768: 100%|██████████| 660/660 [01:45<00:00,  6.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.64it/s]
                   all        393       9029      0.964      0.979      0.991      0.908
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     29/100      6.58G     0.6115     0.4563     0.8267        219        320: 100%|██████████| 660/660 [01:42<00:00,  6.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.32it/s]
                   all        393       9029      0.964      0.972       0.99      0.908

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     30/100      5.97G     0.6097     0.4507     0.8243        130        448: 100%|██████████| 660/660 [01:37<00:00,  6.77it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.26it/s]
                   all        393       9029      0.964      0.982       0.99      0.912

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     31/100      6.82G     0.5985     0.4399     0.8243        279        320: 100%|██████████| 660/660 [01:41<00:00,  6.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.35it/s]
                   all        393       9029      0.974      0.965      0.989      0.914

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     32/100      7.26G     0.5926     0.4313     0.8241        183        672: 100%|██████████| 660/660 [01:42<00:00,  6.46it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.35it/s]
                   all        393       9029      0.975      0.966      0.988      0.914

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     33/100      6.67G     0.5897     0.4314      0.822        176        640: 100%|██████████| 660/660 [01:43<00:00,  6.38it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.27it/s]
                   all        393       9029      0.966      0.974      0.991      0.913
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     34/100       6.5G     0.5825     0.4221     0.8208        227        768: 100%|██████████| 660/660 [01:41<00:00,  6.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.17it/s]
                   all        393       9029      0.971      0.976       0.99      0.914

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     35/100      7.67G     0.5745     0.4127     0.8197        134        320: 100%|██████████| 660/660 [01:40<00:00,  6.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.03it/s]
                   all        393       9029      0.974      0.971      0.991      0.915

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     36/100      7.38G     0.5768     0.4196     0.8206        125        576: 100%|██████████| 660/660 [01:44<00:00,  6.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:03<00:00,  8.25it/s]
                   all        393       9029      0.978      0.965       0.99      0.915
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     37/100      7.79G     0.5732     0.4106     0.8192        196        480: 100%|██████████| 660/660 [03:17<00:00,  3.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.82it/s]
                   all        393       9029      0.968      0.974      0.992      0.917

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     38/100      6.89G     0.5702     0.4113     0.8202        266        352: 100%|██████████| 660/660 [01:44<00:00,  6.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.30it/s]
                   all        393       9029      0.964      0.972       0.99       0.92

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     39/100      7.41G       0.56     0.4013     0.8182        422        736: 100%|██████████| 660/660 [01:43<00:00,  6.40it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.49it/s]
                   all        393       9029      0.974      0.962       0.99      0.919
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     40/100      7.83G     0.5648     0.4102     0.8172        241        480: 100%|██████████| 660/660 [02:09<00:00,  5.11it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.78it/s]
                   all        393       9029      0.972      0.982      0.991      0.922
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     41/100      7.04G      0.556     0.3976     0.8154        256        704: 100%|██████████| 660/660 [01:41<00:00,  6.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.31it/s]
                   all        393       9029      0.974      0.971      0.991      0.925

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     42/100      6.51G     0.5588     0.4005     0.8164        250        704: 100%|██████████| 660/660 [01:39<00:00,  6.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.34it/s]
                   all        393       9029      0.977      0.966       0.99      0.925

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     43/100      7.29G     0.5551     0.3996      0.816        227        768: 100%|██████████| 660/660 [01:42<00:00,  6.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.18it/s]
                   all        393       9029       0.98      0.967      0.991      0.925
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     44/100      6.92G     0.5386     0.3807     0.8135        325        320: 100%|██████████| 660/660 [01:41<00:00,  6.47it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.36it/s]
                   all        393       9029      0.978      0.964       0.99      0.928

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     45/100      6.48G     0.5492     0.3944     0.8153        124        480: 100%|██████████| 660/660 [01:41<00:00,  6.47it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.76it/s]
                   all        393       9029      0.977      0.967      0.991      0.929

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     46/100      6.04G      0.544     0.3864     0.8129        218        512: 100%|██████████| 660/660 [01:40<00:00,  6.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.25it/s]
                   all        393       9029      0.964      0.976      0.991      0.923

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     47/100      7.16G      0.541     0.3867     0.8141        221        800: 100%|██████████| 660/660 [01:44<00:00,  6.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.34it/s]
                   all        393       9029      0.979      0.966       0.99      0.928

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     48/100      6.77G     0.5342     0.3742     0.8139        143        704: 100%|██████████| 660/660 [01:43<00:00,  6.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.04it/s]
                   all        393       9029      0.977      0.967      0.989      0.928
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     49/100      5.98G     0.5386     0.3832     0.8116        205        736: 100%|██████████| 660/660 [01:36<00:00,  6.86it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.33it/s]
                   all        393       9029      0.968       0.98      0.991      0.929

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     50/100      6.59G     0.5292     0.3807     0.8103        216        960: 100%|██████████| 660/660 [01:39<00:00,  6.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.08it/s]
                   all        393       9029      0.974      0.976       0.99      0.932
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     51/100      6.91G     0.5253     0.3704     0.8112        172        416: 100%|██████████| 660/660 [01:43<00:00,  6.40it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.05it/s]
                   all        393       9029       0.95      0.986      0.991      0.933
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     52/100      6.57G     0.5235     0.3697     0.8111        323        576: 100%|██████████| 660/660 [01:40<00:00,  6.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.06it/s]
                   all        393       9029      0.978      0.967      0.991       0.93
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     53/100      6.71G     0.5172     0.3646     0.8105        188        800: 100%|██████████| 660/660 [01:43<00:00,  6.40it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.34it/s]
                   all        393       9029      0.982      0.965       0.99      0.931
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     54/100      7.89G     0.5173     0.3657     0.8104        271        896: 100%|██████████| 660/660 [01:43<00:00,  6.36it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.18it/s]
                   all        393       9029       0.98      0.964       0.99      0.934

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     55/100      6.13G     0.5168     0.3665     0.8099        223        864: 100%|██████████| 660/660 [01:43<00:00,  6.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.22it/s]
                   all        393       9029      0.982      0.967       0.99      0.934

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     56/100      7.28G     0.5153     0.3609     0.8093        192        512: 100%|██████████| 660/660 [01:41<00:00,  6.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.28it/s]
                   all        393       9029      0.977      0.971      0.991      0.936
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     57/100      7.12G     0.5061     0.3566     0.8079        301        832: 100%|██████████| 660/660 [01:43<00:00,  6.37it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.05it/s]
                   all        393       9029      0.984      0.963      0.991      0.937

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     58/100       6.8G     0.5204     0.3702     0.8089        187        384: 100%|██████████| 660/660 [01:38<00:00,  6.72it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.32it/s]
                   all        393       9029      0.977      0.968      0.991      0.936
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     59/100      7.28G      0.511     0.3587     0.8092        237        768: 100%|██████████| 660/660 [01:44<00:00,  6.31it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.12it/s]
                   all        393       9029      0.979      0.967      0.991      0.938

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     60/100       6.9G     0.5076     0.3577     0.8074        280        416: 100%|██████████| 660/660 [01:41<00:00,  6.52it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.33it/s]
                   all        393       9029      0.971      0.971      0.991      0.937

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     61/100      6.92G     0.5063     0.3553     0.8075        206        512: 100%|██████████| 660/660 [01:41<00:00,  6.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.02it/s]
                   all        393       9029      0.979      0.966      0.992      0.935
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     62/100      7.32G     0.5029     0.3561     0.8056        295        736: 100%|██████████| 660/660 [01:39<00:00,  6.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.09it/s]
                   all        393       9029      0.981      0.966       0.99      0.939

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     63/100      8.65G     0.4914     0.3416     0.8055        146        512: 100%|██████████| 660/660 [01:44<00:00,  6.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.32it/s]
                   all        393       9029      0.971      0.974      0.991       0.94

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     64/100      7.03G     0.4938     0.3407     0.8061        167        320: 100%|██████████| 660/660 [01:44<00:00,  6.31it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.34it/s]
                   all        393       9029      0.969       0.98      0.991       0.94

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     65/100      7.79G     0.4889     0.3379     0.8058        170        384: 100%|██████████| 660/660 [01:45<00:00,  6.25it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.74it/s]
                   all        393       9029      0.981      0.966      0.991      0.939
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     66/100      7.84G     0.4872     0.3358     0.8058        237        512: 100%|██████████| 660/660 [01:46<00:00,  6.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.97it/s]
                   all        393       9029      0.955      0.985      0.992      0.939

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     67/100      7.57G     0.4843     0.3374     0.8053        366        832: 100%|██████████| 660/660 [01:41<00:00,  6.48it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.19it/s]
                   all        393       9029       0.98       0.97      0.991      0.942

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     68/100      8.06G     0.4841     0.3359     0.8048        127        800: 100%|██████████| 660/660 [05:41<00:00,  1.93it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:05<00:00,  4.69it/s]
                   all        393       9029      0.973      0.971      0.991      0.943

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     69/100      6.84G     0.4828     0.3327     0.8037        227        864: 100%|██████████| 660/660 [01:41<00:00,  6.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.31it/s]
                   all        393       9029      0.982      0.966      0.991       0.94

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     70/100      6.63G     0.4796     0.3284     0.8043        248        928: 100%|██████████| 660/660 [01:45<00:00,  6.28it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:03<00:00,  8.19it/s]
                   all        393       9029      0.979       0.97      0.991      0.942
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     71/100      7.92G     0.4807     0.3294     0.8036        154        800: 100%|██████████| 660/660 [01:42<00:00,  6.41it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.72it/s]
                   all        393       9029      0.971      0.976      0.991      0.942

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     72/100      6.53G     0.4752      0.325     0.8025        216        576: 100%|██████████| 660/660 [01:40<00:00,  6.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.87it/s]
                   all        393       9029      0.982      0.967      0.991      0.944

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     73/100       6.9G     0.4761     0.3306      0.803        170        736: 100%|██████████| 660/660 [01:40<00:00,  6.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.38it/s]
                   all        393       9029      0.982      0.967      0.992      0.945
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     74/100      6.33G      0.476     0.3279     0.8022        307        544: 100%|██████████| 660/660 [01:39<00:00,  6.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.14it/s]
                   all        393       9029      0.983      0.965      0.992      0.944
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     75/100      5.83G     0.4709     0.3225     0.8028        265        896: 100%|██████████| 660/660 [01:40<00:00,  6.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.49it/s]
                   all        393       9029       0.98      0.967      0.991      0.944
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     76/100      7.18G     0.4698     0.3204     0.8021        267        736: 100%|██████████| 660/660 [01:41<00:00,  6.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.43it/s]
                   all        393       9029      0.984      0.966      0.991      0.945

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     77/100      6.95G     0.4616     0.3138     0.8015        192        544: 100%|██████████| 660/660 [01:46<00:00,  6.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:03<00:00,  8.08it/s]
                   all        393       9029      0.983      0.966      0.991      0.945
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     78/100      7.95G     0.4614     0.3138     0.8002        207        512: 100%|██████████| 660/660 [01:47<00:00,  6.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.29it/s]
                   all        393       9029      0.983      0.967      0.991      0.945

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     79/100      8.13G     0.4647     0.3195     0.8023        265        864: 100%|██████████| 660/660 [03:27<00:00,  3.18it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.38it/s]
                   all        393       9029      0.984      0.966      0.991      0.945
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     80/100      6.81G     0.4629     0.3224     0.8011        364        512: 100%|██████████| 660/660 [01:39<00:00,  6.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.18it/s]
                   all        393       9029      0.982      0.966      0.992      0.945
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     81/100      6.67G     0.4595     0.3138     0.8005        194        800: 100%|██████████| 660/660 [01:41<00:00,  6.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.47it/s]
                   all        393       9029       0.98      0.969      0.991      0.945
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     82/100      6.33G     0.4559     0.3104     0.8001        264        608: 100%|██████████| 660/660 [01:39<00:00,  6.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.51it/s]
                   all        393       9029      0.983      0.964      0.991      0.946

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     83/100      6.36G     0.4598     0.3167     0.8004        172        544: 100%|██████████| 660/660 [01:40<00:00,  6.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.66it/s]
                   all        393       9029      0.955       0.99      0.992      0.946

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     84/100      6.66G      0.452     0.3083     0.7994        246        608: 100%|██████████| 660/660 [01:40<00:00,  6.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.29it/s]
                   all        393       9029      0.954       0.99      0.992      0.946

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     85/100      7.06G     0.4525     0.3081     0.7983        293        768: 100%|██████████| 660/660 [01:38<00:00,  6.67it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.34it/s]
                   all        393       9029       0.98      0.972      0.991      0.947
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     86/100      6.47G     0.4514     0.3074     0.8002        152        608: 100%|██████████| 660/660 [01:40<00:00,  6.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.03it/s]
                   all        393       9029      0.975      0.972      0.992      0.948

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     87/100      6.82G     0.4485     0.3037     0.7991        296        928: 100%|██████████| 660/660 [01:39<00:00,  6.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.15it/s]
                   all        393       9029      0.984      0.968      0.991      0.947
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     88/100      7.29G     0.4497     0.3061     0.7997        356        672: 100%|██████████| 660/660 [01:41<00:00,  6.47it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.40it/s]
                   all        393       9029      0.985      0.966      0.992       0.95
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     89/100      6.77G     0.4474      0.305     0.7983        168        640: 100%|██████████| 660/660 [01:39<00:00,  6.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.19it/s]
                   all        393       9029      0.985      0.967      0.991      0.949

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     90/100      6.33G     0.4485     0.3079     0.8007        292        672: 100%|██████████| 660/660 [01:40<00:00,  6.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.22it/s]
                   all        393       9029      0.966      0.983      0.991       0.95
Closing dataloader mosaic
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     91/100      5.47G     0.3212     0.1997     0.7778         74        832: 100%|██████████| 660/660 [01:37<00:00,  6.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.45it/s]
                   all        393       9029       0.96      0.989      0.992      0.951

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     92/100      5.57G     0.3085     0.1905     0.7764         62        960: 100%|██████████| 660/660 [01:34<00:00,  7.00it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.96it/s]
                   all        393       9029      0.955      0.989      0.992      0.954
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     93/100      5.65G     0.3023      0.188     0.7752         61        352: 100%|██████████| 660/660 [01:36<00:00,  6.86it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  8.56it/s]
                   all        393       9029       0.98      0.973      0.992      0.954
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     94/100      5.42G     0.2968      0.184     0.7753         79        672: 100%|██████████| 660/660 [01:34<00:00,  6.98it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.19it/s]
                   all        393       9029      0.947      0.993      0.992      0.954

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     95/100      5.64G     0.2935     0.1832     0.7744         81        544: 100%|██████████| 660/660 [01:35<00:00,  6.92it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.64it/s]
                   all        393       9029      0.986      0.969      0.992      0.955
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     96/100       5.5G     0.2928     0.1828     0.7747         86        512: 100%|██████████| 660/660 [01:34<00:00,  6.99it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.40it/s]
                   all        393       9029      0.948      0.994      0.992      0.955
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     97/100      5.51G     0.2861     0.1782     0.7743         75        416: 100%|██████████| 660/660 [01:35<00:00,  6.89it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.46it/s]
                   all        393       9029      0.985      0.969      0.992      0.955
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     98/100      5.38G      0.286     0.1772     0.7742         71        672: 100%|██████████| 660/660 [01:36<00:00,  6.84it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.52it/s]
                   all        393       9029      0.984      0.969      0.991      0.957
  0%|          | 0/660 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     99/100      5.64G     0.2812     0.1753     0.7739         80        544: 100%|██████████| 660/660 [01:40<00:00,  6.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.23it/s]
                   all        393       9029      0.985      0.967      0.991      0.956

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    100/100      5.92G     0.2805     0.1746     0.7732         75        960: 100%|██████████| 660/660 [01:35<00:00,  6.92it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:02<00:00,  9.57it/s]
                   all        393       9029      0.984      0.967      0.991      0.957

100 epochs completed in 3.084 hours.
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100\weights\last.pt, 19.3MB
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100\weights\best.pt, 19.3MB

Validating C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100\weights\best.pt...
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11s summary (fused): 100 layers, 9,483,234 parameters, 0 gradients, 21.7 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 25/25 [00:05<00:00,  4.78it/s]
                   all        393       9029      0.984      0.967      0.991      0.935
                   ACM         40         40      0.996          1      0.995      0.995
                   ALB         67         83      0.999          1      0.995      0.918
                   AMI          7         12       0.98          1      0.995      0.995
           API-Gateway        200        304      0.997      0.985      0.995      0.956
Active Directory Service         36         36      0.995          1      0.995      0.954
              Airflow_          3          6      0.976          1      0.995      0.974
               Amplify         16         16      0.989          1      0.995      0.817
    Analytics Services          5          5          1          1      0.995      0.995
               AppFlow         25         25      0.993          1      0.995      0.981
               Appsync          6          6      0.972          1      0.995      0.678
                Athena         36         37      0.995          1      0.995      0.925
                Aurora         44         54      0.996          1      0.995      0.975
          Auto Scaling         48         73      0.999          1      0.995      0.934
    Auto Scaling Group          4         10      0.987          1      0.995      0.898
       Automated Tests         15         20      0.992          1      0.995      0.924
     Availability Zone         12         24      0.993          1      0.995      0.974
                Backup          3          6      0.975          1      0.995      0.995
     Build Environment          7          7      0.983          1      0.995      0.852
                   CDN          5          5      0.964          1      0.995      0.995
                   CUR          5          5          1          1      0.995      0.711
          Call Metrics         25         25      0.995          1      0.995      0.974
       Call Recordings         25         25      0.995          1      0.995      0.908
   Certificate Manager         43         43      0.996          1      0.995      0.992
                Client          3         13          1      0.609      0.995      0.995
       Cloud Connector         11         22      0.993          1      0.995      0.971
             Cloud Map          5          5      0.968          1      0.995      0.995
          Cloud Search         19         19      0.992          1      0.995      0.976
           Cloud Trail         53         53      0.977      0.981      0.989      0.942
           Cloud Watch        113        135      0.998          1      0.995      0.939
  CloudFormation Stack         32         37      0.995          1      0.995      0.988
              CloudHSM         30         30          1      0.973      0.995      0.941
      CloudWatch Alarm         18         23      0.994          1      0.995      0.931
            Cloudfront        102        108      0.996          1      0.995      0.948
             CodeBuild         30         50      0.997          1      0.995      0.958
            CodeCommit         17         17       0.99          1      0.995      0.974
            CodeDeploy          5          5      0.967          1      0.995      0.978
          CodePipeline         43         43      0.995          1      0.995      0.902
               Cognito         90        104      0.979      0.962      0.969       0.95
            Comprehend         25         25      0.993          1      0.995      0.995
                Config         38        163      0.987          1      0.984       0.86
               Connect         25         25      0.993          1      0.995      0.986
  Connect Contact Lens         25         25      0.996          1      0.995      0.936
             Container         17         66      0.999          1      0.995      0.917
         Control Tower          5          5      0.967          1      0.995      0.932
      Customer Gateway          8         11      0.986          1      0.995      0.995
                   DSI          5         10          1          1      0.995      0.862
         Data Pipeline          5          5          1      0.846      0.995       0.82
              DataSync          5          5          1          1      0.995      0.995
          Deploy Stage         10         10      0.985          1      0.995      0.811
             Detective         25         25      0.993          1      0.995      0.956
        Direct Connect         21         21      0.992          1      0.995      0.991
          Distribution          5          5          1      0.592      0.995      0.995
          Docker Image         21         72          1          1      0.995      0.837
             Dynamo DB        169        263      0.999          1      0.995      0.957
                   EBS         27         37      0.996          1      0.995      0.918
                   EC2        179        418      0.995       0.96      0.991       0.93
                   EFS         22         30      0.964      0.967      0.963      0.929
      EFS Mount Target         52        102      0.971       0.99      0.986      0.907
                   EKS         53         59       0.98      0.983      0.995      0.972
                   ELB        111        150      0.999      0.933      0.966      0.933
                   EMR         10         10      0.983          1      0.995      0.903
         Edge Location          5          7      0.978          1      0.995      0.995
           ElastiCache         22         26      0.993          1      0.995      0.969
Elastic Container Registry         43         43      0.996          1      0.995      0.966
Elastic Container Service         50         60      0.981      0.983      0.978      0.857
        Elastic Search         38         38      0.995          1      0.995      0.929
Elemental MediaConvert         16         18      0.942          1      0.992      0.947
Elemental MediaPackage          5          5          1      0.845      0.995      0.995
                 Email          5          5      0.971          1      0.995       0.93
              Endpoint          5          5      0.971          1      0.995      0.894
             Event Bus          5          5      0.968          1      0.995      0.995
           EventBridge         35        135      0.999          1      0.995       0.89
   Experiment Duration          7          7          1          0      0.995      0.922
           Experiments          7          7          1          0      0.978      0.977
               Fargate         29         71      0.999          1      0.995      0.923
Fault Injection Simulator         15         15      0.989          1      0.995      0.868
      Firewall Manager         25         25      0.993          1      0.995      0.993
                 Flask          8         24      0.997          1      0.995      0.834
             Flow logs         25        100          1          1      0.995       0.85
              GameLift          5          5       0.97          1      0.995      0.903
                   Git          8          8       0.98          1      0.995      0.967
                Github         17         18      0.991          1      0.995      0.966
               Glacier         10         10      0.983          1      0.995      0.943
                  Glue         19         38      0.994          1      0.995      0.968
         Glue DataBrew          7          7      0.977          1      0.995      0.995
               Grafana         10         10      0.983          1      0.995      0.995
             GuardDuty         34        134      0.999          1      0.995      0.961
                   IAM         66        207      0.998      0.981      0.995      0.909
              IAM Role         41        169      0.988      0.972      0.983        0.8
              IOT Core         13         17       0.99          1      0.995      0.989
                 Image         11         11       0.99          1      0.995      0.844
         Image Builder          5          5      0.968          1      0.995      0.995
               Ingress          5          5      0.969          1      0.995      0.904
       Inspector Agent         25         25      0.993          1      0.995      0.986
             Instances          3          6      0.537      0.395      0.641      0.641
              Internet         59         82      0.917          1      0.993      0.937
      Internet Gateway         51         87          1       0.99      0.995      0.887
               Jenkins          3          6      0.976          1      0.995      0.957
Key Management Service         47         75      0.996          1      0.995      0.981
                Kibana          7          7      0.981          1      0.995      0.957
  Kinesis Data Streams         72         85      0.988       0.99      0.989      0.958
            Kubernetes          8          8      0.982          1      0.995      0.977
                Lambda        255        675      0.999      0.994      0.995      0.961
                   Lex          5          5      0.966          1      0.995      0.995
                    MQ          6         12      0.993          1      0.995      0.889
      Machine Learning          9          9      0.959          1      0.995      0.995
                 Macie         45        110      0.999          1      0.995      0.921
           Marketplace          5          5      0.989          1      0.995      0.764
             Memcached          5         10      0.983          1      0.995      0.962
         Mobile Client         36         41      0.998          1      0.995      0.913
              Mongo DB         11         23      0.947          1      0.995      0.868
                 MySQL          7          7      0.983          1      0.995      0.932
           NAT Gateway         44         85      0.983          1      0.994      0.977
               Neptune          5          5      0.966          1      0.995       0.59
       Network Adapter          5          5      0.968          1      0.995      0.995
      Network Firewall         25         25      0.993          1      0.995       0.95
              Notebook          5          5       0.97          1      0.995      0.995
      Order Controller          5          5      0.977          1      0.995       0.88
    Organization Trail         30        105      0.999          1      0.995      0.877
       Parameter Store          7          7       0.98          1      0.995       0.95
              Pinpoint          5          5      0.966          1      0.995      0.974
            PostgreSQL          7          7      0.979          1      0.995      0.951
          Private Link         25         25      0.993          1      0.995      0.958
        Private Subnet        106        263      0.923       0.97      0.984       0.89
            Prometheus         10         10      0.983          1      0.995      0.995
         Public Subnet        104        216      0.973      0.989      0.994      0.888
               Quarkus         10         10      0.983          1      0.995      0.988
            Quicksight         32         34      0.995          1      0.995      0.995
                   RDS         93        197          1          1      0.995      0.962
                 React          3          3      0.964          1      0.995      0.866
                 Redis         10         21      0.992          1      0.995      0.963
              Redshift         45         46      0.996      0.978      0.994      0.922
                Region         36         53      0.997          1      0.995      0.872
           Rekognition         14         14      0.987          1      0.995      0.948
               Results          7          7          1          0      0.862      0.862
              Route 53         40         40      0.996          1      0.995       0.98
               Route53         87        138      0.989          1      0.995       0.96
                    S3        260        514      0.996      0.981      0.991      0.938
                   SAR          5          5          1          1      0.995      0.983
                   SDK         26         88          1      0.946      0.995      0.928
                   SES         14         17      0.991          1      0.995      0.949
                   SNS         62         69          1      0.974      0.989      0.969
                   SQS         43         44      0.998          1      0.995      0.975
             SSM Agent         25         25      0.993          1      0.995       0.91
             Sagemaker         18         61          1      0.558      0.957      0.741
        Secret Manager         30         30      0.994          1      0.995      0.882
        Security Group          5          5       0.97          1      0.995      0.995
          Security Hub         30        130      0.999          1      0.995      0.871
                Server         27         42      0.997          1      0.995      0.924
       Service Catalog          8         23      0.993          1      0.995      0.952
                Shield         31         31      0.994          1      0.995      0.928
               Sign-On         25         25          1          1      0.995      0.991
                 Slack         12         12      0.987          1      0.995      0.982
              Snowball         10         10      0.983          1      0.995      0.995
                 Stack          5          5       0.97          1      0.995      0.831
         Step Function          7         21      0.988          1      0.995      0.972
       Storage Gateway         10         10      0.983          1      0.995      0.985
            SwaggerHub          3          3      0.952          1      0.995      0.995
       Systems Manager         39         64      0.993          1      0.995      0.976
                    TV          5          5      0.971          1      0.995      0.939
                 Table         20         40      0.995          1      0.995      0.956
           Task Runner          5          5      0.968          1      0.995      0.927
             Terraform         13         13       0.99          1      0.995      0.957
             Text File         14         32          1      0.964      0.994      0.941
              Textract          3          3       0.95          1      0.995      0.995
            Transcribe          9          9      0.982          1      0.995      0.995
       Transfer Family         16         16      0.989          1      0.995      0.991
       Transit Gateway         10         10      0.983          1      0.995      0.948
             Translate         19         19      0.991          1      0.995      0.973
       Trusted Advisor          5          5      0.969          1      0.995      0.924
                Twilio          7          7      0.976          1      0.995      0.995
                 Users        152        204          1          1      0.995      0.932
                   VDA         11         11      0.985          1      0.995      0.969
            VP Gateway          6          7      0.983          1      0.995       0.98
            VPC Router          9         16      0.992          1      0.995      0.894
        VPN Connection          5          8      0.981          1      0.995      0.983
                   WAF         43         46      0.996          1      0.995      0.979
           Web Clients         45         62          1      0.763      0.994      0.893
              Websites          5          5      0.971          1      0.995      0.873
                 X-Ray         16         20      0.991          1      0.995      0.964
                   aws        240        322      0.997      0.997      0.995      0.936
          cache Worker          8          8       0.98          1      0.995       0.98
Speed: 0.1ms preprocess, 9.0ms inference, 0.0ms loss, 1.8ms postprocess per image
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100
🚀 Save dir: C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100
✅ best.pt:  C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11s_custom_100\weights\best.pt
Ultralytics 8.3.161  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11s summary (fused): 100 layers, 9,483,234 parameters, 0 gradients, 21.7 GFLOPs
val: Fast image access  (ping: 0.00.0 ms, read: 91.124.6 MB/s, size: 343.9 KB)
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels.cache... 386 images, 0 backgrounds, 0 corrupt: 100%|██████████| 386/386 [00:00<?, ?it/s]
                                           0% | 0.00/18.42 MB [00:00<?, ?MB/s]: 
                                            0% | 0.00/0.46 MB [00:00<?, ?MB/s]: 

                                            0% | 0.00/0.44 MB [00:00<?, ?MB/s]: 


                                            0% | 0.00/0.43 MB [00:00<?, ?MB/s]: 


████████████████████████████████▍  98% | 0.42/0.43 MB [00:00<00:00,  2.26s/MB]: 

█████████████████████████████████ 100% | 0.44/0.44 MB [00:00<00:00,  2.23s/MB]: 
████████████████████████████████▌  99% | 0.45/0.46 MB [00:01<00:00,  2.42s/MB]: 



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   0%|          | 0/49 [00:00<?, ?it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   2%|▏         | 1/49 [00:00<00:15,  3.03it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   4%|▍         | 2/49 [00:00<00:10,  4.44it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   6%|▌         | 3/49 [00:00<00:08,  5.50it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   8%|▊         | 4/49 [00:00<00:07,  5.86it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  12%|█▏        | 6/49 [00:00<00:05,  8.56it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  18%|█▊        | 9/49 [00:01<00:03, 12.27it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  24%|██▍       | 12/49 [00:01<00:02, 14.01it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  29%|██▊       | 14/49 [00:01<00:02, 14.77it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  35%|███▍      | 17/49 [00:01<00:01, 16.18it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  39%|███▉      | 19/49 [00:01<00:01, 16.90it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  43%|████▎     | 21/49 [00:01<00:01, 17.57it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  47%|████▋     | 23/49 [00:01<00:01, 17.56it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  51%|█████     | 25/49 [00:01<00:01, 15.34it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  55%|█████▌    | 27/49 [00:02<00:01, 16.01it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  59%|█████▉    | 29/49 [00:02<00:01, 15.71it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  63%|██████▎   | 31/49 [00:02<00:01, 14.35it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  67%|██████▋   | 33/49 [00:02<00:01, 14.52it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  71%|███████▏  | 35/49 [00:02<00:00, 15.06it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  76%|███████▌  | 37/49 [00:02<00:00, 14.59it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  80%|███████▉  | 39/49 [00:02<00:00, 14.37it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  84%|████████▎ | 41/49 [00:03<00:00, 14.00it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  88%|████████▊ | 43/49 [00:03<00:00, 14.07it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  92%|█████████▏| 45/49 [00:03<00:00, 14.05it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  96%|█████████▌| 47/49 [00:03<00:00, 13.38it/s]



                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 49/49 [00:03<00:00, 13.29it/s]
█████████████▏                    41% | 7.59/18.42 MB [00:10<00:14,  1.33s/MB]:                    all        386       7672      0.981      0.955      0.986      0.957
                   ACM         22         22      0.991          1      0.995      0.995
                   ALB         58         74          1      0.951      0.994      0.956
                   AMI          8         13      0.957          1      0.995      0.995
           API-Gateway        201        304      0.993      0.985      0.994      0.983
Active Directory Service         15         15      0.987          1      0.995      0.995
              Airflow_          3          6      0.971          1      0.995      0.995
               Amplify         18         18      0.988          1      0.995      0.972
    Analytics Services          5          5          1          1      0.995      0.968
               AppFlow         12         12      0.984          1      0.995      0.995
               Appsync          8          8      0.976          1      0.995      0.926
                Athena         32         33      0.993          1      0.995      0.984
                Aurora         27         36      0.993      0.889       0.93      0.921
          Auto Scaling         45         75          1      0.966      0.994       0.93
    Auto Scaling Group          3          8      0.979          1      0.995      0.914
       Automated Tests         12         17      0.989          1      0.995      0.942
     Availability Zone         10         20      0.991          1      0.995      0.995
                Backup          3          6      0.969          1      0.995      0.995
     Build Environment          6          6      0.975          1      0.995      0.834
                   CDN          7          7      0.973          1      0.995      0.951
                   CUR          6          6      0.968          1      0.995      0.961
          Call Metrics         12         12      0.985          1      0.995       0.98
       Call Recordings         12         12          1          1      0.995      0.941
   Certificate Manager         28         28      0.992          1      0.995      0.995
                Client          3          8          1      0.359      0.778      0.772
       Cloud Connector          7         14      0.986          1      0.995      0.984
             Cloud Map          5          5      0.959          1      0.995      0.995
          Cloud Search         14         14      0.987          1      0.995      0.987
           Cloud Trail         39         41       0.96      0.976      0.984      0.965
           Cloud Watch        126        151      0.999          1      0.995      0.955
  CloudFormation Stack         38         45      0.995          1      0.995      0.989
              CloudHSM         13         13          1      0.941      0.995      0.991
      CloudWatch Alarm         18         23      0.992          1      0.995      0.944
            Cloudfront         97        101      0.996       0.98      0.995      0.969
             CodeBuild         33         53      0.997          1      0.995      0.982
            CodeCommit         15         15      0.987          1      0.995      0.986
            CodeDeploy          5          5       0.96          1      0.995      0.947
          CodePipeline         43         43      0.973          1      0.993      0.954
               Cognito         85        100      0.998       0.98      0.986      0.982
            Comprehend         27         27      0.992          1      0.995      0.995
                Config         25         65      0.967          1      0.972      0.972
               Connect         12         12      0.982          1      0.995      0.995
  Connect Contact Lens         12         12          1          1      0.995      0.987
             Container         18         81      0.995          1      0.995      0.941
         Control Tower          7          7          1          1      0.995      0.995
      Customer Gateway          5         11      0.982          1      0.995      0.971
                   DSI          5         10      0.986          1      0.995       0.85
         Data Pipeline          5          5          1      0.852      0.995      0.995
              DataSync          5          5      0.962          1      0.995      0.995
          Deploy Stage          7          7      0.975          1      0.995       0.81
             Detective          8          8      0.975          1      0.995      0.995
        Direct Connect         19         26      0.992      0.962      0.976      0.895
          Distribution          5          5          1      0.708      0.962      0.962
          Docker Image         18         61          1      0.954      0.975       0.88
             Dynamo DB        174        270      0.999       0.97      0.989      0.963
                   EBS         24         36          1      0.979      0.995      0.958
                   EC2        166        406       0.99      0.948      0.989      0.932
                   EFS         28         36      0.943      0.923      0.941      0.914
      EFS Mount Target         35         54       0.98      0.897      0.936      0.928
                   EKS         51         58      0.983      0.987      0.995      0.989
                   ELB        104        149      0.999       0.94      0.973       0.95
                   EMR          5          5      0.965          1      0.995      0.995
         Edge Location          3          5      0.967          1      0.995      0.773
           ElastiCache         25         31          1      0.879       0.96      0.942
Elastic Container Registry         51         51      0.996          1      0.995      0.994
Elastic Container Service         50         62      0.981      0.952      0.984      0.899
        Elastic Search         32         33      0.995          1      0.995      0.962
Elemental MediaConvert         17         20      0.829          1      0.979      0.977
Elemental MediaPackage          5          5          1      0.261      0.858      0.858
                 Email          5          5          1      0.842      0.995      0.948
              Endpoint          6          6      0.915          1      0.995      0.928
             Event Bus          5          5      0.962          1      0.995      0.995
           EventBridge         21         53      0.996          1      0.995      0.993
   Experiment Duration          5          5          1          0      0.879      0.765
           Experiments          5          5          1          0      0.928      0.892
               Fargate         30         72      0.998          1      0.995      0.957
Fault Injection Simulator         12         12          1          1      0.995      0.884
      Firewall Manager          8          8          1          1      0.995      0.995
                 Flask          6         18      0.996          1      0.995      0.937
             Flow logs          8         32      0.995          1      0.995      0.953
              GameLift          5          5      0.962          1      0.995      0.928
                   Git          6          6      0.968          1      0.995      0.984
                Github         20         25      0.992          1      0.995       0.98
               Glacier          5          5      0.963          1      0.995      0.995
                  Glue         15         30      0.994          1      0.995      0.971
         Glue DataBrew          7          7      0.971          1      0.995      0.995
               Grafana          8          8      0.975          1      0.995      0.995
             GuardDuty         17         49      0.996          1      0.995      0.993
                   IAM         51        104          1      0.954      0.989      0.958
              IAM Role         25         68      0.966      0.941      0.979       0.89
              IOT Core         12         14      0.996          1      0.995      0.991
                 Image         13         13      0.989          1      0.995      0.953
         Image Builder          5          5      0.956          1      0.995      0.995
               Ingress          5          5      0.959          1      0.995      0.995
       Inspector Agent          8          8      0.975          1      0.995      0.995
             Instances          3          6      0.552      0.421      0.701      0.676
              Internet         63         86      0.922      0.966      0.988      0.961
      Internet Gateway         32         50      0.991          1      0.995      0.938
               Jenkins          3          6      0.971          1      0.995      0.966
Key Management Service         29         40      0.996          1      0.995      0.995
                Kibana          7          7      0.977          1      0.995      0.995
  Kinesis Data Streams         50         66      0.984      0.946      0.993      0.988
            Kubernetes          6          6      0.972          1      0.995      0.995
                Lambda        243        673          1      0.995      0.995      0.985
                   Lex          5          5      0.961          1      0.995      0.995
                    MQ          5         11      0.991          1      0.995      0.884
      Machine Learning         11         11          1      0.773      0.995      0.975
                 Macie         27         70      0.997          1      0.995      0.979
           Marketplace          5          5          1          1      0.995      0.709
             Memcached          6         12      0.982          1      0.995      0.935
         Mobile Client         40         49      0.998          1      0.995      0.935
              Mongo DB          9         21      0.996          1      0.995      0.892
                 MySQL          7          7      0.979          1      0.995      0.959
           NAT Gateway         46         88      0.966      0.943      0.979      0.957
               Neptune          6          6          1          1      0.995      0.897
       Network Adapter          5          5       0.96          1      0.995      0.995
      Network Firewall          8          8      0.976          1      0.995      0.995
              Notebook          5          5      0.963          1      0.995      0.995
      Order Controller          5          5       0.95          1      0.995      0.934
    Organization Trail         17         41      0.995          1      0.995      0.989
       Parameter Store          7          7      0.976          1      0.995      0.995
              Pinpoint          5          5      0.959          1      0.995      0.995
            PostgreSQL          7          7      0.975          1      0.995      0.973
          Private Link         24         24      0.991          1      0.995      0.995
        Private Subnet         89        208      0.995      0.957      0.978      0.918
            Prometheus          8          8      0.975          1      0.995      0.995
         Public Subnet         90        203      0.985      0.958      0.981        0.9
               Quarkus          8          8          1          1      0.995      0.995
            Quicksight         19         21       0.99          1      0.995      0.995
                   RDS         83        163      0.953      0.945      0.949      0.928
                 React          4          4      0.968          1      0.995      0.962
                 Redis         10         25       0.99       0.96      0.968      0.964
              Redshift         27         29          1      0.973      0.995      0.991
                Region         36         52      0.998          1      0.995      0.925
           Rekognition         14         14      0.986          1      0.995      0.995
               Results          5          5          1          0      0.879      0.863
              Route 53         21         21      0.946          1       0.95       0.95
               Route53         98        167      0.987      0.994      0.994      0.974
                    S3        256        520      0.998      0.981      0.995      0.969
                   SAR          5          5          1          1      0.995      0.995
                   SDK         24         80      0.987      0.979      0.991       0.95
                   SES         17         20          1      0.994      0.995      0.978
                   SNS         63         69          1      0.974      0.995      0.982
                   SQS         49         50      0.997          1      0.995      0.977
             SSM Agent          8          8          1          1      0.995      0.995
             Sagemaker         16         59          1      0.457      0.972      0.837
        Secret Manager         14         14      0.985          1      0.995      0.995
        Security Group          5          5       0.96          1      0.995      0.899
          Security Hub         13         45      0.996          1      0.995      0.993
                Server         20         32      0.994          1      0.995      0.899
       Service Catalog         10         31      0.994          1      0.995      0.956
                Shield         15         15      0.986          1      0.995      0.995
               Sign-On          8          8          1          1      0.995      0.995
                 Slack         13         13      0.986          1      0.995      0.995
              Snowball          5          5      0.963          1      0.995      0.995
                 Stack          5          5      0.969          1      0.995      0.995
         Step Function          8         24      0.986          1      0.995      0.924
       Storage Gateway          5          5          1          1      0.995      0.995
            SwaggerHub          5          5          1          1      0.995      0.995
       Systems Manager         20         28      0.992          1      0.995      0.993
                    TV          6          6      0.977          1      0.995      0.982
                 Table         23         46      0.995          1      0.995      0.978
           Task Runner          5          5       0.96          1      0.995      0.995
             Terraform         11         11      0.984          1      0.995      0.982
             Text File         11         28      0.844      0.966      0.921       0.89
              Textract          5          5          1          1      0.995      0.995
            Transcribe          9          9      0.977          1      0.995      0.995
       Transfer Family         15         15      0.987          1      0.995      0.992
       Transit Gateway         12         12      0.983          1      0.995      0.995
             Translate         19         19      0.989          1      0.995      0.995
       Trusted Advisor          6          6          1          1      0.995      0.968
                Twilio          7          7       0.97          1      0.995      0.995
                 Users        144        196          1      0.997      0.995       0.96
                   VDA          7          7      0.973          1      0.995      0.995
            VP Gateway          5          6      0.982      0.833      0.972      0.947
            VPC Router          8         16      0.984          1      0.995      0.902
        VPN Connection          3          9      0.993          1      0.995       0.96
                   WAF         25         28      0.992          1      0.995      0.982
           Web Clients         50         62          1      0.794      0.989      0.916
              Websites          9          9      0.961          1      0.995      0.937
                 X-Ray         19         21       0.99          1      0.995      0.991
                   aws        243        326      0.994      0.988      0.995      0.956
          cache Worker          7          7      0.972          1      0.995      0.995
Speed: 0.2ms preprocess, 5.2ms inference, 0.0ms loss, 1.2ms postprocess per image
Saving C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val\predictions.json...
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val

🎯 Test Metrics (mean per class):
  Precision:    0.981
  Recall:       0.955
  mAP@0.5:      0.986
  mAP@0.5:0.95: 0.957

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_02.png: 576x640 2 Cloud Watchs, 1 Cloudfront, 4 EC2s, 1 ElastiCache, 1 Key Management Service, 1 NAT Gateway, 3 Private Subnets, 3 Public Subnets, 2 RDSs, 1 Region, 2 S3s, 1 SES, 1 Users, 2 WAFs, 1 aws, 84.3ms
Speed: 4.9ms preprocess, 84.3ms inference, 8.0ms postprocess per image at shape (1, 3, 576, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict\labels
✅ Detailed JSON saved to data\reports\yolo11s_custom_100\results.json
✅ Summary JSON saved to data\reports\yolo11s_custom_100\report.json
([ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
names: {0: 'ACM', 1: 'ALB', 2: 'AMI', 3: 'API-Gateway', 4: 'Active Directory Service', 5: 'Airflow_', 6: 'Amplify', 7: 'Analytics Services', 8: 'AppFlow', 9: 'Appsync', 10: 'Athena', 11: 'Aurora', 12: 'Auto Scaling', 13: 'Auto Scaling Group', 14: 'Automated Tests', 15: 'Availability Zone', 16: 'Backup', 17: 'Build Environment', 18: 'CDN', 19: 'CUR', 20: 'Call Metrics', 21: 'Call Recordings', 22: 'Certificate Manager', 23: 'Client', 24: 'Cloud Connector', 25: 'Cloud Map', 26: 'Cloud Search', 27: 'Cloud Trail', 28: 'Cloud Watch', 29: 'CloudFormation Stack', 30: 'CloudHSM', 31: 'CloudWatch Alarm', 32: 'Cloudfront', 33: 'CodeBuild', 34: 'CodeCommit', 35: 'CodeDeploy', 36: 'CodePipeline', 37: 'Cognito', 38: 'Comprehend', 39: 'Config', 40: 'Connect', 41: 'Connect Contact Lens', 42: 'Container', 43: 'Control Tower', 44: 'Customer Gateway', 45: 'DSI', 46: 'Data Pipeline', 47: 'DataSync', 48: 'Deploy Stage', 49: 'Detective', 50: 'Direct Connect', 51: 'Distribution', 52: 'Docker Image', 53: 'Dynamo DB', 54: 'EBS', 55: 'EC2', 56: 'EFS', 57: 'EFS Mount Target', 58: 'EKS', 59: 'ELB', 60: 'EMR', 61: 'Edge Location', 62: 'ElastiCache', 63: 'Elastic Container Registry', 64: 'Elastic Container Service', 65: 'Elastic Search', 66: 'Elemental MediaConvert', 67: 'Elemental MediaPackage', 68: 'Email', 69: 'Endpoint', 70: 'Event Bus', 71: 'EventBridge', 72: 'Experiment Duration', 73: 'Experiments', 74: 'Fargate', 75: 'Fault Injection Simulator', 76: 'Firewall Manager', 77: 'Flask', 78: 'Flow logs', 79: 'GameLift', 80: 'Git', 81: 'Github', 82: 'Glacier', 83: 'Glue', 84: 'Glue DataBrew', 85: 'Grafana', 86: 'GuardDuty', 87: 'IAM', 88: 'IAM Role', 89: 'IOT Core', 90: 'Image', 91: 'Image Builder', 92: 'Ingress', 93: 'Inspector Agent', 94: 'Instances', 95: 'Internet', 96: 'Internet Gateway', 97: 'Jenkins', 98: 'Key Management Service', 99: 'Kibana', 100: 'Kinesis Data Streams', 101: 'Kubernetes', 102: 'Lambda', 103: 'Lex', 104: 'MQ', 105: 'Machine Learning', 106: 'Macie', 107: 'Marketplace', 108: 'Memcached', 109: 'Mobile Client', 110: 'Mongo DB', 111: 'MySQL', 112: 'NAT Gateway', 113: 'Neptune', 114: 'Network Adapter', 115: 'Network Firewall', 116: 'Notebook', 117: 'Order Controller', 118: 'Organization Trail', 119: 'Parameter Store', 120: 'Pinpoint', 121: 'PostgreSQL', 122: 'Private Link', 123: 'Private Subnet', 124: 'Prometheus', 125: 'Public Subnet', 126: 'Quarkus', 127: 'Quicksight', 128: 'RDS', 129: 'React', 130: 'Redis', 131: 'Redshift', 132: 'Region', 133: 'Rekognition', 134: 'Results', 135: 'Route 53', 136: 'Route53', 137: 'S3', 138: 'SAR', 139: 'SDK', 140: 'SES', 141: 'SNS', 142: 'SQS', 143: 'SSM Agent', 144: 'Sagemaker', 145: 'Secret Manager', 146: 'Security Group', 147: 'Security Hub', 148: 'Server', 149: 'Service Catalog', 150: 'Shield', 151: 'Sign-On', 152: 'Slack', 153: 'Snowball', 154: 'Stack', 155: 'Step Function', 156: 'Storage Gateway', 157: 'SwaggerHub', 158: 'Systems Manager', 159: 'TV', 160: 'Table', 161: 'Task Runner', 162: 'Terraform', 163: 'Text File', 164: 'Textract', 165: 'Transcribe', 166: 'Transfer Family', 167: 'Transit Gateway', 168: 'Translate', 169: 'Trusted Advisor', 170: 'Twilio', 171: 'Users', 172: 'VDA', 173: 'VP Gateway', 174: 'VPC Router', 175: 'VPN Connection', 176: 'WAF', 177: 'Web Clients', 178: 'Websites', 179: 'X-Ray', 180: 'aws', 181: 'cache Worker'}
obb: None
orig_img: array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)
orig_shape: (993, 1167)
path: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_02.png'
probs: None
save_dir: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\runs\\detect\\predict'
speed: {'preprocess': 4.903499997453764, 'inference': 84.32300001732074, 'postprocess': 8.02300000214018}],
 [{'boxes': [{'class': 176,
              'confidence': 0.9682163596153259,
              'coordinates': [650.6542358398438,
                              39.00212860107422,
                              741.3566284179688,
                              130.7328338623047],
              'name': 'WAF'},
             {'class': 176,
              'confidence': 0.9589774012565613,
              'coordinates': [384.0617370605469,
                              38.26711654663086,
                              475.09271240234375,
                              130.67282104492188],
              'name': 'WAF'},
             {'class': 128,
              'confidence': 0.9556941390037537,
              'coordinates': [411.3981628417969,
                              755.106689453125,
                              500.1042175292969,
                              843.8895263671875],
              'name': 'RDS'},
             {'class': 128,
              'confidence': 0.954138457775116,
              'coordinates': [255.6346893310547,
                              755.2382202148438,
                              341.19244384765625,
                              843.5369262695312],
              'name': 'RDS'},
             {'class': 28,
              'confidence': 0.9537869691848755,
              'coordinates': [969.572998046875,
                              213.7010498046875,
                              1058.7939453125,
                              300.9198913574219],
              'name': 'Cloud Watch'},
             {'class': 55,
              'confidence': 0.9502649307250977,
              'coordinates': [759.7893676757812,
                              758.8599243164062,
                              849.4012451171875,
                              848.4196166992188],
              'name': 'EC2'},
             {'class': 125,
              'confidence': 0.9459349513053894,
              'coordinates': [401.08795166015625,
                              313.547607421875,
                              446.44818115234375,
                              359.7774963378906],
              'name': 'Public Subnet'},
             {'class': 125,
              'confidence': 0.9452306032180786,
              'coordinates': [691.8026123046875,
                              313.68572998046875,
                              736.2325439453125,
                              360.0868835449219],
              'name': 'Public Subnet'},
             {'class': 98,
              'confidence': 0.944023072719574,
              'coordinates': [971.7753295898438,
                              345.1828308105469,
                              1054.2257080078125,
                              429.4676208496094],
              'name': 'Key Management Service'},
             {'class': 125,
              'confidence': 0.9350648522377014,
              'coordinates': [134.20179748535156,
                              319.6605529785156,
                              179.7294464111328,
                              363.8770751953125],
              'name': 'Public Subnet'},
             {'class': 180,
              'confidence': 0.9262549877166748,
              'coordinates': [71.30086517333984,
                              148.70989990234375,
                              109.833251953125,
                              189.8184356689453],
              'name': 'aws'},
             {'class': 171,
              'confidence': 0.925313413143158,
              'coordinates': [131.13597106933594,
                              50.710933685302734,
                              197.52468872070312,
                              115.77574157714844],
              'name': 'Users'},
             {'class': 123,
              'confidence': 0.9230290651321411,
              'coordinates': [135.34707641601562,
                              453.436279296875,
                              178.2580108642578,
                              495.12359619140625],
              'name': 'Private Subnet'},
             {'class': 32,
              'confidence': 0.9200432896614075,
              'coordinates': [505.1424865722656,
                              39.99667739868164,
                              594.0325927734375,
                              128.9741668701172],
              'name': 'Cloudfront'},
             {'class': 123,
              'confidence': 0.9194516539573669,
              'coordinates': [402.79022216796875,
                              452.7129821777344,
                              445.880615234375,
                              496.31976318359375],
              'name': 'Private Subnet'},
             {'class': 28,
              'confidence': 0.9188613891601562,
              'coordinates': [971.1754150390625,
                              624.3637084960938,
                              1057.3280029296875,
                              710.41943359375],
              'name': 'Cloud Watch'},
             {'class': 132,
              'confidence': 0.9078757166862488,
              'coordinates': [83.54353332519531,
                              188.06658935546875,
                              123.3695297241211,
                              230.6660614013672],
              'name': 'Region'},
             {'class': 123,
              'confidence': 0.9032012224197388,
              'coordinates': [692.4966430664062,
                              452.13916015625,
                              736.358642578125,
                              495.6383361816406],
              'name': 'Private Subnet'},
             {'class': 140,
              'confidence': 0.8645418286323547,
              'coordinates': [970.8497924804688,
                              768.8991088867188,
                              1057.1756591796875,
                              855.9013061523438],
              'name': 'SES'},
             {'class': 62,
              'confidence': 0.8421372771263123,
              'coordinates': [545.809814453125,
                              753.7843627929688,
                              634.9067993164062,
                              843.88134765625],
              'name': 'ElastiCache'},
             {'class': 55,
              'confidence': 0.7935768961906433,
              'coordinates': [195.204833984375,
                              558.6671142578125,
                              286.7924499511719,
                              649.4301147460938],
              'name': 'EC2'},
             {'class': 137,
              'confidence': 0.7892306447029114,
              'coordinates': [972.9020385742188,
                              500.4378662109375,
                              1056.5308837890625,
                              582.798828125],
              'name': 'S3'},
             {'class': 55,
              'confidence': 0.7836862802505493,
              'coordinates': [482.8027038574219,
                              562.4357299804688,
                              574.3709716796875,
                              653.0350952148438],
              'name': 'EC2'},
             {'class': 112,
              'confidence': 0.7727504372596741,
              'coordinates': [776.01123046875,
                              357.0038757324219,
                              838.7301025390625,
                              416.0096130371094],
              'name': 'NAT Gateway'},
             {'class': 55,
              'confidence': 0.7596423625946045,
              'coordinates': [761.4385375976562,
                              561.9155883789062,
                              851.9475708007812,
                              653.5723876953125],
              'name': 'EC2'},
             {'class': 137,
              'confidence': 0.7572213411331177,
              'coordinates': [146.35353088378906,
                              757.0053100585938,
                              232.7991485595703,
                              842.3672485351562],
              'name': 'S3'}],
   'path': 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_02.png'}])
███████████████████████████████ 100% | 18.42/18.42 MB [00:37<00:00,  2.04s/MB]: 
Skipping upload, could not find object file 'C:\Users\acmattos\AppData\Local\Temp\tmpvdulyi2c.png'
Skipping upload, could not find object file 'C:\Users\acmattos\AppData\Local\Temp\tmpbvmejhr1.png'
Skipping upload, could not find object file 'C:\Users\acmattos\AppData\Local\Temp\tmpcngu7t7_.png'
████████████████████████████████ 100% | 0.46/0.46 MB [05:04<00:00, 662.03s/MB]: 
████████████████████████████████ 100% | 0.44/0.44 MB [05:04<00:00, 692.12s/MB]: 
████████████████████████████████ 100% | 0.43/0.43 MB [05:04<00:00, 708.22s/MB]: 
```
Report
```bash
C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\.venv\Scripts\python.exe C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\report.py 

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_01.jpg: 544x640 1 Dynamo DB, 5 Lambdas, 1 S3, 1 SNS, 2 Userss, 1 aws, 55.0ms
Speed: 2.3ms preprocess, 55.0ms inference, 67.7ms postprocess per image at shape (1, 3, 544, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict2
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict2\labels
✅ Detailed JSON saved to data\reports\yolo11s_custom_200\results.json
✅ Summary JSON saved to data\reports\yolo11s_custom_200\report.json
Reports generated: data/reports/yolo11s_custom_200
```

