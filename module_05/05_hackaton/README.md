yolo11n
```bash
C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\.venv\Scripts\python.exe C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\model.py 
True
New https://pypi.org/project/ultralytics/8.3.157 available  Update with 'pip install -U ultralytics'
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
engine\trainer: agnostic_nms=False, amp=True, augment=True, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data/dataset/aws/data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=200, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.01, lrf=0.05, mask_ratio=4, max_det=300, mixup=0.5, mode=train, model=./data/model/yolo11n.pt, momentum=0.937, mosaic=1.0, multi_scale=True, name=yolo11n_custom_200, nbs=64, nms=False, opset=None, optimize=False, optimizer=AdamW, overlap_mask=True, patience=40, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, save=True, save_conf=False, save_crop=False, save_dir=C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
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
ClearML Task: created new task id=63cd0f81cbeb4a03951f810806826bca
ClearML results page: https://app.clear.ml/projects/14f0119248fa451f826c387955b212a3/experiments/63cd0f81cbeb4a03951f810806826bca/output/log
WARNING ClearML Initialized a new task. If you want to run remotely, please add clearml-init and connect your arguments before initializing YOLO.
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
Downloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt to 'yolo11n.pt'...
100%|██████████| 5.35M/5.35M [00:03<00:00, 1.77MB/s]
AMP: checks passed 
train: Fast image access  (ping: 0.00.0 ms, read: 97.760.3 MB/s, size: 80.2 KB)
train: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\train\labels.cache... 478 images, 0 backgrounds, 0 corrupt: 100%|██████████| 478/478 [00:00<?, ?it/s]
WARNING Box and segment counts should be equal, but got len(segments) = 1356, len(boxes) = 7878. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\valid\labels.cache... 2 images, 0 backgrounds, 0 corrupt: 100%|██████████| 2/2 [00:00<?, ?it/s]
val: Fast image access  (ping: 0.00.0 ms, read: 118.261.5 MB/s, size: 235.6 KB)
WARNING Error decoding JSON from C:\Users\acmattos\AppData\Roaming\Ultralytics\persistent_cache.json. Starting with an empty dictionary.
Plotting labels to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\labels.jpg... 
optimizer: AdamW(lr=0.01, momentum=0.937) with parameter groups 81 weight(decay=0.0), 88 weight(decay=0.0005), 87 bias(decay=0.0)
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200
Starting training for 200 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      1/200      4.08G      1.446      4.368      1.207        189        352: 100%|██████████| 60/60 [00:42<00:00,  1.41it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  1.61it/s]
                   all          2         62          0          0          0          0
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      2/200      3.79G      1.451      3.408      1.246        230        800: 100%|██████████| 60/60 [00:26<00:00,  2.29it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.33it/s]
                   all          2         62     0.0963     0.0217    0.00837    0.00328

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      3/200      3.81G      1.408      3.163      1.282        248        768: 100%|██████████| 60/60 [00:24<00:00,  2.45it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  3.73it/s]
                   all          2         62     0.0844     0.0494     0.0392     0.0156

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      4/200      3.82G      1.351      2.954      1.222        225        480: 100%|██████████| 60/60 [00:23<00:00,  2.53it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.09it/s]
                   all          2         62     0.0908      0.429       0.28      0.105
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      5/200      3.82G      1.337      2.841      1.211        262        480: 100%|██████████| 60/60 [00:21<00:00,  2.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.71it/s]
                   all          2         62      0.151      0.428       0.28      0.117

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      6/200      3.82G      1.332      2.677      1.224        169        512: 100%|██████████| 60/60 [00:23<00:00,  2.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.69it/s]
                   all          2         62      0.455      0.337      0.349      0.145
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      7/200      3.84G      1.314       2.57      1.187        157        832: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  8.06it/s]
                   all          2         62      0.463      0.408      0.393      0.158

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      8/200      3.84G      1.302       2.47      1.206        306        640: 100%|██████████| 60/60 [00:23<00:00,  2.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.13it/s]
                   all          2         62      0.228      0.761      0.499      0.217

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      9/200      3.84G       1.28      2.439      1.221        291        928: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.74it/s]
                   all          2         62      0.314      0.712      0.582      0.241
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     10/200      3.84G      1.255       2.35      1.202        234        704: 100%|██████████| 60/60 [00:23<00:00,  2.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.02it/s]
                   all          2         62      0.579      0.405      0.463      0.178
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     11/200      3.84G      1.204      2.227      1.171        199        736: 100%|██████████| 60/60 [00:23<00:00,  2.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.45it/s]
                   all          2         62      0.256      0.606      0.529      0.239

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     12/200      3.84G      1.241      2.249      1.182        251        800: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.91it/s]
                   all          2         62      0.244      0.693      0.552      0.237
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     13/200      3.84G      1.196       2.17      1.194        240        896: 100%|██████████| 60/60 [00:23<00:00,  2.52it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.45it/s]
                   all          2         62      0.409      0.717      0.676      0.299

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     14/200      3.84G      1.229      2.179      1.189        301        608: 100%|██████████| 60/60 [00:22<00:00,  2.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.71it/s]
                   all          2         62      0.531      0.739      0.766      0.362

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     15/200      3.84G      1.227      2.117      1.204        199        960: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.94it/s]
                   all          2         62      0.352      0.833       0.66      0.302
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     16/200      3.84G      1.203      2.005      1.163        209        640: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.58it/s]
                   all          2         62      0.753      0.427      0.635      0.278
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     17/200      3.85G      1.232      1.985      1.148        242        864: 100%|██████████| 60/60 [00:23<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.74it/s]
                   all          2         62      0.443      0.641      0.698      0.341
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     18/200      3.85G      1.204      1.989      1.167        237        704: 100%|██████████| 60/60 [00:22<00:00,  2.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.61it/s]
                   all          2         62      0.413      0.842      0.797      0.383

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     19/200      3.85G      1.194      1.912      1.185        190        640: 100%|██████████| 60/60 [00:21<00:00,  2.74it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.55it/s]
                   all          2         62      0.292      0.674      0.587      0.264
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     20/200      3.85G      1.206      1.942      1.186        197        928: 100%|██████████| 60/60 [00:23<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.12it/s]
                   all          2         62      0.513      0.718      0.726      0.317

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     21/200      3.85G      1.192      1.892      1.148        270        832: 100%|██████████| 60/60 [00:22<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.63it/s]
                   all          2         62      0.635      0.576      0.786      0.391
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     22/200      3.85G      1.211      1.884      1.171        263        480: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.55it/s]
                   all          2         62      0.417      0.909      0.794       0.36
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     23/200      3.85G        1.2      1.844      1.145        127        736: 100%|██████████| 60/60 [00:22<00:00,  2.71it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.69it/s]
                   all          2         62      0.452      0.957      0.796      0.371

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     24/200      3.85G      1.161      1.779      1.108        312        480: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.11it/s]
                   all          2         62      0.378      0.957      0.826      0.387
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     25/200      4.18G      1.177      1.803       1.17        245        672: 100%|██████████| 60/60 [00:23<00:00,  2.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.67it/s]
                   all          2         62      0.642      0.647      0.799      0.368
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     26/200      3.72G      1.208       1.82      1.162        384        544: 100%|██████████| 60/60 [00:23<00:00,  2.55it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.52it/s]
                   all          2         62      0.574      0.796      0.789      0.374
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     27/200       4.3G      1.162      1.769      1.133        212        960: 100%|██████████| 60/60 [00:21<00:00,  2.77it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.78it/s]
                   all          2         62      0.438      0.834       0.75      0.336

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     28/200      3.71G      1.168      1.777      1.156        339        416: 100%|██████████| 60/60 [00:22<00:00,  2.67it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.59it/s]
                   all          2         62      0.623      0.681      0.805      0.374

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     29/200      3.96G      1.158       1.74      1.147        346        672: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.96it/s]
                   all          2         62      0.702      0.721      0.863      0.421
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     30/200      4.19G      1.174      1.765      1.139        331        480: 100%|██████████| 60/60 [00:22<00:00,  2.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.31it/s]
                   all          2         62       0.55      0.812      0.808      0.382

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     31/200      3.85G      1.147      1.709      1.145        270        576: 100%|██████████| 60/60 [00:23<00:00,  2.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.41it/s]
                   all          2         62      0.648      0.593      0.775      0.367

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     32/200      3.86G      1.157      1.749      1.171        315        704: 100%|██████████| 60/60 [00:22<00:00,  2.68it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.46it/s]
                   all          2         62      0.608      0.734      0.837      0.406

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     33/200      4.23G      1.173      1.748      1.138        274        320: 100%|██████████| 60/60 [00:23<00:00,  2.54it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.65it/s]
                   all          2         62       0.49      0.726      0.707      0.316
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     34/200      3.84G      1.143      1.668      1.129        220        960: 100%|██████████| 60/60 [00:22<00:00,  2.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.92it/s]
                   all          2         62      0.637      0.726      0.836      0.395
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     35/200      3.85G      1.164      1.706      1.146        220        672: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.99it/s]
                   all          2         62      0.528      0.721      0.806       0.41

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     36/200      3.87G      1.168      1.666      1.131        197        352: 100%|██████████| 60/60 [00:21<00:00,  2.73it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.50it/s]
                   all          2         62      0.743      0.751      0.834      0.404

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     37/200      4.25G      1.177      1.672       1.17        263        896: 100%|██████████| 60/60 [00:22<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.84it/s]
                   all          2         62      0.486      0.902       0.82      0.386
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     38/200      4.07G      1.169      1.651      1.137        238        672: 100%|██████████| 60/60 [00:22<00:00,  2.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.37it/s]
                   all          2         62      0.638      0.662      0.821      0.413
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     39/200       3.5G      1.134      1.606      1.132        260        544: 100%|██████████| 60/60 [00:24<00:00,  2.47it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.01it/s]
                   all          2         62      0.603      0.771      0.788      0.381

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     40/200      3.78G      1.154       1.59      1.156        248        704: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.31it/s]
                   all          2         62      0.567      0.748      0.804      0.371

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     41/200      4.16G      1.171      1.607      1.155        215        320: 100%|██████████| 60/60 [00:22<00:00,  2.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.65it/s]
                   all          2         62      0.653      0.718      0.768      0.367
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     42/200      4.15G      1.162      1.656      1.168        311        608: 100%|██████████| 60/60 [00:23<00:00,  2.56it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.74it/s]
                   all          2         62      0.555      0.924      0.801      0.397

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     43/200      3.93G      1.149       1.57       1.13        184        768: 100%|██████████| 60/60 [00:22<00:00,  2.63it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.73it/s]
                   all          2         62      0.681      0.701      0.845      0.421

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     44/200      4.22G      1.121      1.547      1.123        207        864: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.92it/s]
                   all          2         62      0.571      0.737      0.688      0.345

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     45/200      4.03G       1.13      1.575      1.127        197        544: 100%|██████████| 60/60 [00:21<00:00,  2.75it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.00it/s]
                   all          2         62      0.593      0.704      0.744      0.327

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     46/200      3.73G      1.136      1.607      1.145        209        960: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.96it/s]
                   all          2         62      0.704       0.68      0.877      0.411
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     47/200      4.01G      1.138      1.568      1.124        233        864: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.42it/s]
                   all          2         62      0.621       0.81      0.864      0.403
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     48/200      3.43G      1.122      1.559      1.099        291        576: 100%|██████████| 60/60 [00:22<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.79it/s]
                   all          2         62      0.517      0.902      0.864      0.379
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     49/200      3.68G      1.114      1.525      1.112        348        928: 100%|██████████| 60/60 [00:22<00:00,  2.72it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.48it/s]
                   all          2         62      0.635      0.717      0.821      0.378
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     50/200      3.69G      1.129      1.554      1.137        216        832: 100%|██████████| 60/60 [00:22<00:00,  2.68it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.77it/s]
                   all          2         62      0.666      0.671      0.783      0.388
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     51/200      4.25G      1.119      1.532      1.112        176        416: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  5.01it/s]
                   all          2         62      0.597      0.804      0.846      0.391
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     52/200      3.67G      1.118      1.534      1.106        232        768: 100%|██████████| 60/60 [00:23<00:00,  2.58it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.58it/s]
                   all          2         62      0.735       0.74      0.878      0.435
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     53/200      3.68G      1.126      1.517      1.126        195        544: 100%|██████████| 60/60 [00:22<00:00,  2.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.06it/s]
                   all          2         62      0.665      0.822      0.854      0.421

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     54/200       3.7G      1.137      1.499      1.135        279        544: 100%|██████████| 60/60 [00:21<00:00,  2.73it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.97it/s]
                   all          2         62      0.751       0.71      0.917      0.464
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     55/200      4.04G       1.11      1.408      1.106        138        896: 100%|██████████| 60/60 [00:22<00:00,  2.65it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.74it/s]
                   all          2         62      0.788      0.728      0.876      0.408

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     56/200      3.55G      1.144      1.511      1.144        331        544: 100%|██████████| 60/60 [00:23<00:00,  2.61it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.62it/s]
                   all          2         62      0.761      0.823        0.9       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     57/200      4.11G      1.117      1.424       1.12        196        640: 100%|██████████| 60/60 [00:22<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.11it/s]
                   all          2         62      0.866       0.68       0.86      0.421

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     58/200      3.89G      1.105      1.445      1.098        181        448: 100%|██████████| 60/60 [00:22<00:00,  2.64it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  7.38it/s]
                   all          2         62      0.757      0.778      0.887      0.421
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     59/200      4.17G      1.124      1.484      1.114        253        704: 100%|██████████| 60/60 [00:23<00:00,  2.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.60it/s]
                   all          2         62      0.633      0.848      0.907      0.457
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     60/200      3.48G      1.089      1.414      1.112        310        480: 100%|██████████| 60/60 [00:23<00:00,  2.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.51it/s]
                   all          2         62      0.632      0.761       0.88      0.404
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     61/200      3.71G      1.102      1.409      1.113        265        544: 100%|██████████| 60/60 [00:23<00:00,  2.59it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.96it/s]
                   all          2         62      0.729      0.813      0.873      0.428
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     62/200      3.98G       1.14       1.48      1.129        242        800: 100%|██████████| 60/60 [00:23<00:00,  2.57it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.55it/s]
                   all          2         62       0.72      0.772      0.886      0.437
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     63/200      4.65G      1.084      1.383      1.086        359        864: 100%|██████████| 60/60 [00:09<00:00,  6.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.89it/s]
                   all          2         62      0.683      0.799      0.906      0.452

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     64/200      3.92G      1.112      1.452      1.126        185        672: 100%|██████████| 60/60 [00:06<00:00,  8.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.41it/s]
                   all          2         62      0.737      0.803       0.88      0.431

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     65/200      3.93G       1.08      1.377       1.11        261        352: 100%|██████████| 60/60 [00:06<00:00,  8.91it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.78it/s]
                   all          2         62      0.652      0.872      0.929      0.454
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     66/200      3.93G      1.112      1.399       1.09        163        800: 100%|██████████| 60/60 [00:07<00:00,  8.52it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.76it/s]
                   all          2         62      0.637      0.869      0.923      0.449
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     67/200      4.26G      1.074       1.34      1.098        493        544: 100%|██████████| 60/60 [00:06<00:00,  8.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.02it/s]
                   all          2         62      0.672      0.861       0.89      0.402
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     68/200      4.32G      1.084      1.351      1.112        255        544: 100%|██████████| 60/60 [00:06<00:00,  8.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.49it/s]
                   all          2         62      0.755        0.8       0.86      0.409
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     69/200      3.66G      1.103      1.435      1.099        169        544: 100%|██████████| 60/60 [00:06<00:00,  9.79it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62      0.664      0.826      0.908      0.444
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     70/200      4.33G      1.084      1.368       1.13        391        928: 100%|██████████| 60/60 [00:07<00:00,  8.01it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.72it/s]
                   all          2         62      0.727      0.832      0.908      0.429

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     71/200      4.04G      1.078      1.351      1.102        189        640: 100%|██████████| 60/60 [00:07<00:00,  8.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 16.20it/s]
                   all          2         62      0.742       0.85      0.906      0.455
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     72/200      3.81G      1.068      1.308       1.09        186        384: 100%|██████████| 60/60 [00:07<00:00,  8.37it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.49it/s]
                   all          2         62      0.661       0.83      0.889      0.428
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     73/200      4.12G      1.079      1.397      1.093        279        896: 100%|██████████| 60/60 [00:06<00:00,  9.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.11it/s]
                   all          2         62      0.858      0.713      0.905      0.466
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     74/200      3.74G      1.107      1.385        1.1        228        800: 100%|██████████| 60/60 [00:06<00:00,  9.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.72it/s]
                   all          2         62      0.679      0.777      0.911      0.444
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     75/200      3.76G      1.095      1.353      1.112        357        608: 100%|██████████| 60/60 [00:06<00:00,  8.69it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 18.65it/s]
                   all          2         62      0.857      0.757      0.943      0.447
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     76/200      3.77G      1.069      1.289      1.111        363        672: 100%|██████████| 60/60 [00:07<00:00,  8.28it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 38.49it/s]
                   all          2         62      0.875       0.72      0.929      0.469
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     77/200      4.08G      1.106      1.377      1.098        263        640: 100%|██████████| 60/60 [00:06<00:00,  8.82it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.71it/s]
                   all          2         62      0.729      0.842      0.887       0.43
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     78/200      4.18G      1.096      1.394      1.101        265        480: 100%|██████████| 60/60 [00:06<00:00,  8.73it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.67it/s]
                   all          2         62      0.738       0.71      0.887      0.429
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     79/200      4.16G      1.085      1.309      1.095        238        800: 100%|██████████| 60/60 [00:07<00:00,  8.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.68it/s]
                   all          2         62      0.656      0.891      0.914       0.44
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     80/200      4.16G      1.072      1.317      1.092        188        672: 100%|██████████| 60/60 [00:06<00:00,  8.91it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 36.22it/s]
                   all          2         62      0.766      0.816      0.937      0.452

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     81/200      4.01G      1.098      1.343       1.12        302        896: 100%|██████████| 60/60 [00:07<00:00,  8.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.08it/s]
                   all          2         62       0.64      0.933      0.893      0.462

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     82/200      3.81G      1.075      1.339      1.095        314        672: 100%|██████████| 60/60 [00:06<00:00,  8.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.25it/s]
                   all          2         62      0.683       0.87       0.93      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     83/200      3.83G      1.104      1.422       1.14        323        640: 100%|██████████| 60/60 [00:07<00:00,  8.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.72it/s]
                   all          2         62      0.691      0.858      0.952      0.464
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     84/200      3.85G      1.088      1.375      1.112        266        704: 100%|██████████| 60/60 [00:06<00:00,  9.12it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.30it/s]
                   all          2         62      0.699      0.815      0.941      0.467

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     85/200      3.85G      1.097      1.327      1.092        225        544: 100%|██████████| 60/60 [00:06<00:00,  9.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.82it/s]
                   all          2         62      0.779      0.829      0.927      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     86/200      3.86G      1.078      1.357      1.106        326        544: 100%|██████████| 60/60 [00:06<00:00,  8.76it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 23.98it/s]
                   all          2         62      0.724      0.899       0.94      0.466

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     87/200      3.88G      1.102      1.318      1.079        315        608: 100%|██████████| 60/60 [00:06<00:00,  9.31it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.48it/s]
                   all          2         62      0.663       0.82      0.891      0.454

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     88/200      4.17G      1.069      1.319      1.094        183        640: 100%|██████████| 60/60 [00:06<00:00,  8.68it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.41it/s]
                   all          2         62      0.701      0.877      0.929      0.459
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     89/200      4.25G      1.052      1.333      1.109        277        832: 100%|██████████| 60/60 [00:07<00:00,  8.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.15it/s]
                   all          2         62      0.833      0.806      0.948      0.482
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     90/200      3.73G      1.072      1.314      1.091        187        480: 100%|██████████| 60/60 [00:06<00:00,  8.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 21.80it/s]
                   all          2         62      0.748      0.899      0.934      0.463

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     91/200      3.98G       1.09       1.32      1.093        160        480: 100%|██████████| 60/60 [00:06<00:00,  8.94it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.43it/s]
                   all          2         62      0.767      0.755      0.917       0.44

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     92/200      4.26G      1.065      1.273      1.091        240        928: 100%|██████████| 60/60 [00:07<00:00,  8.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62      0.715      0.857      0.921      0.464

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     93/200      3.89G      1.057      1.285       1.08        176        800: 100%|██████████| 60/60 [00:06<00:00,  8.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62       0.69      0.844      0.886      0.451

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     94/200      4.19G      1.051      1.266      1.099        216        512: 100%|██████████| 60/60 [00:07<00:00,  7.77it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 16.95it/s]
                   all          2         62      0.701      0.902      0.941      0.477

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     95/200      3.75G      1.068      1.286      1.102        302        384: 100%|██████████| 60/60 [00:07<00:00,  8.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.43it/s]
                   all          2         62      0.698       0.89       0.93      0.482

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     96/200      3.76G      1.083      1.355      1.089        312        640: 100%|██████████| 60/60 [00:06<00:00,  8.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 26.66it/s]
                   all          2         62      0.792      0.819      0.905      0.448
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     97/200      3.77G      1.061      1.297      1.088        186        640: 100%|██████████| 60/60 [00:07<00:00,  8.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.09it/s]
                   all          2         62      0.671      0.889      0.916      0.433

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     98/200      3.77G      1.051       1.25      1.111        188        320: 100%|██████████| 60/60 [00:07<00:00,  7.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.64it/s]
                   all          2         62      0.742      0.908      0.952      0.459
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     99/200      3.79G      1.053        1.3      1.082        245        480: 100%|██████████| 60/60 [00:06<00:00,  8.78it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 21.31it/s]
                   all          2         62      0.696       0.87       0.93      0.478

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    100/200      4.12G      1.044       1.21      1.081        295        864: 100%|██████████| 60/60 [00:07<00:00,  8.37it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 25.95it/s]
                   all          2         62      0.689      0.778      0.926      0.454

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    101/200      4.39G      1.066      1.238      1.107        362        416: 100%|██████████| 60/60 [00:08<00:00,  7.48it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.18it/s]
                   all          2         62        0.7      0.886      0.917      0.447
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    102/200       3.3G      1.037       1.22      1.079        263        800: 100%|██████████| 60/60 [00:07<00:00,  8.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.33it/s]
                   all          2         62      0.704      0.913      0.944      0.473

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    103/200      3.73G       1.04      1.193      1.092        249        640: 100%|██████████| 60/60 [00:07<00:00,  7.92it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 23.32it/s]
                   all          2         62      0.667      0.855      0.914       0.46
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    104/200      3.74G       1.05      1.242      1.106        332        864: 100%|██████████| 60/60 [00:07<00:00,  8.13it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.42it/s]
                   all          2         62      0.881      0.825      0.952      0.474

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    105/200      3.74G       1.05      1.258      1.079        223        832: 100%|██████████| 60/60 [00:07<00:00,  8.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.20it/s]
                   all          2         62      0.661      0.839      0.914      0.446

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    106/200      3.76G      1.063      1.207      1.093        281        640: 100%|██████████| 60/60 [00:07<00:00,  8.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.30it/s]
                   all          2         62      0.761      0.938      0.948      0.472
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    107/200      4.39G      1.054      1.226      1.077        305        640: 100%|██████████| 60/60 [00:07<00:00,  8.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.59it/s]
                   all          2         62      0.666      0.913      0.915      0.447

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    108/200      4.16G      1.047      1.226      1.083        333        832: 100%|██████████| 60/60 [00:07<00:00,  7.94it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 19.38it/s]
                   all          2         62       0.73      0.905      0.952      0.494
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    109/200      3.53G      1.055      1.213      1.043        276        320: 100%|██████████| 60/60 [00:06<00:00,  9.04it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.19it/s]
                   all          2         62      0.758      0.865      0.948      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    110/200      3.84G      1.038      1.185      1.089        223        384: 100%|██████████| 60/60 [00:07<00:00,  8.50it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 24.43it/s]
                   all          2         62      0.808      0.804      0.931      0.485
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    111/200      3.86G      1.038      1.223      1.097        236        416: 100%|██████████| 60/60 [00:06<00:00,  8.71it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62        0.8      0.785      0.923      0.456
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    112/200      3.87G      1.029       1.19      1.074        286        384: 100%|██████████| 60/60 [00:07<00:00,  8.49it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 35.71it/s]
                   all          2         62      0.673      0.874      0.906      0.469

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    113/200      3.87G      1.049       1.19       1.09        218        416: 100%|██████████| 60/60 [00:07<00:00,  8.09it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.48it/s]
                   all          2         62      0.722      0.931      0.933      0.451
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    114/200      3.88G      1.047      1.235      1.097        305        320: 100%|██████████| 60/60 [00:06<00:00,  8.62it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.47it/s]
                   all          2         62      0.773      0.935      0.942      0.465

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    115/200      4.26G      1.059       1.24      1.101        145        512: 100%|██████████| 60/60 [00:07<00:00,  8.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.77it/s]
                   all          2         62      0.676      0.945      0.949      0.483

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    116/200       3.5G       1.05      1.214      1.077        242        320: 100%|██████████| 60/60 [00:07<00:00,  8.13it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.42it/s]
                   all          2         62      0.759      0.908      0.947      0.469

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    117/200      3.74G      1.034      1.173      1.073        162        672: 100%|██████████| 60/60 [00:07<00:00,  7.89it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 23.26it/s]
                   all          2         62      0.801       0.95      0.952      0.476

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    118/200      3.99G      1.035      1.193       1.09        229        832: 100%|██████████| 60/60 [00:07<00:00,  8.16it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.13it/s]
                   all          2         62      0.727      0.817      0.873      0.433
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    119/200      4.31G      1.028      1.164      1.084        296        480: 100%|██████████| 60/60 [00:07<00:00,  8.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.31it/s]
                   all          2         62      0.738      0.952      0.946      0.475
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    120/200      3.79G      1.012       1.13      1.089        265        672: 100%|██████████| 60/60 [00:07<00:00,  8.08it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.26it/s]
                   all          2         62      0.827      0.827      0.922      0.465
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    121/200      4.02G      1.014      1.144      1.061        328        960: 100%|██████████| 60/60 [00:07<00:00,  8.26it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.29it/s]
                   all          2         62      0.727      0.929      0.931       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    122/200      3.86G      1.065      1.222      1.084        222        896: 100%|██████████| 60/60 [00:07<00:00,  8.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.90it/s]
                   all          2         62      0.846      0.829      0.924      0.468

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    123/200      3.88G      1.048       1.22      1.087        204        864: 100%|██████████| 60/60 [00:06<00:00,  8.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.42it/s]
                   all          2         62      0.697      0.902      0.941      0.461
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    124/200      3.89G      1.028      1.148      1.075        290        576: 100%|██████████| 60/60 [00:07<00:00,  8.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.83it/s]
                   all          2         62      0.772       0.89      0.922      0.463

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    125/200      3.89G      1.054      1.219      1.097        237        448: 100%|██████████| 60/60 [00:07<00:00,  8.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62      0.747      0.952      0.952       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    126/200      3.89G       1.04      1.187      1.074        187        672: 100%|██████████| 60/60 [00:06<00:00,  8.66it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 20.00it/s]
                   all          2         62       0.72      0.913      0.952      0.489
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    127/200      4.26G      1.041      1.196      1.083        167        352: 100%|██████████| 60/60 [00:07<00:00,  8.38it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.04it/s]
                   all          2         62      0.715      0.893       0.91      0.461
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    128/200      3.91G      1.043      1.157      1.074        371        352: 100%|██████████| 60/60 [00:07<00:00,  8.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 27.41it/s]
                   all          2         62       0.72      0.944      0.945      0.468
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    129/200      3.91G      1.024       1.14      1.068        198        960: 100%|██████████| 60/60 [00:06<00:00,  8.60it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 17.13it/s]
                   all          2         62      0.732      0.917      0.921       0.47
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    130/200      3.93G      1.018       1.12      1.067        150        512: 100%|██████████| 60/60 [00:07<00:00,  7.94it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.98it/s]
                   all          2         62      0.749      0.849      0.915      0.446

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    131/200      4.19G      1.029      1.181      1.076        272        640: 100%|██████████| 60/60 [00:07<00:00,  8.04it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 28.98it/s]
                   all          2         62      0.803      0.883      0.922      0.452

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    132/200      3.67G      1.026      1.149      1.045        194        672: 100%|██████████| 60/60 [00:06<00:00,  9.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 25.97it/s]
                   all          2         62       0.84      0.786      0.927      0.473
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    133/200      3.97G       1.01      1.101      1.072        231        320: 100%|██████████| 60/60 [00:07<00:00,  8.15it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 31.25it/s]
                   all          2         62      0.862       0.79       0.92      0.458
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    134/200       4.3G      1.013      1.135      1.071        257        736: 100%|██████████| 60/60 [00:07<00:00,  8.51it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 32.26it/s]
                   all          2         62      0.765      0.894      0.934      0.475
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    135/200      3.85G      1.041      1.155      1.058        176        960: 100%|██████████| 60/60 [00:07<00:00,  8.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.93it/s]
                   all          2         62      0.775      0.868      0.932      0.494
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    136/200      3.86G      1.034      1.183      1.068        254        672: 100%|██████████| 60/60 [00:06<00:00,  8.70it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.41it/s]
                   all          2         62      0.747      0.939      0.947      0.477

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    137/200      3.88G      1.018      1.141      1.034        333        512: 100%|██████████| 60/60 [00:06<00:00,  9.72it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.88it/s]
                   all          2         62      0.776      0.941      0.949      0.491
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    138/200      4.22G      1.025       1.14       1.05        229        800: 100%|██████████| 60/60 [00:07<00:00,  8.44it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.49it/s]
                   all          2         62      0.755      0.957      0.941      0.484
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    139/200      3.57G      1.008      1.097      1.057        221        320: 100%|██████████| 60/60 [00:07<00:00,  8.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.48it/s]
                   all          2         62      0.739      0.926      0.924      0.447
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    140/200      4.37G      1.038      1.172       1.09        236        928: 100%|██████████| 60/60 [00:07<00:00,  8.42it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 33.34it/s]
                   all          2         62      0.818      0.861      0.907      0.451

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    141/200       3.8G      1.011      1.102      1.078        276        608: 100%|██████████| 60/60 [00:07<00:00,  8.20it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 34.28it/s]
                   all          2         62      0.863      0.896      0.937      0.476
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    142/200      4.31G      1.005      1.112      1.063        225        448: 100%|██████████| 60/60 [00:07<00:00,  8.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 22.87it/s]
                   all          2         62       0.75      0.897      0.947      0.474
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    143/200      4.03G      1.009      1.083       1.06        295        704: 100%|██████████| 60/60 [00:07<00:00,  8.05it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.76it/s]
                   all          2         62      0.696      0.884      0.927      0.459

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    144/200       3.6G      1.003      1.076      1.043        299        320: 100%|██████████| 60/60 [00:07<00:00,  8.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 29.41it/s]
                   all          2         62      0.804      0.878      0.936      0.466
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    145/200      3.83G      1.037      1.163      1.061        307        576: 100%|██████████| 60/60 [00:06<00:00,  9.11it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.30it/s]
                   all          2         62      0.767      0.925      0.924      0.472

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    146/200      4.08G      1.003      1.065      1.031        255        704: 100%|██████████| 60/60 [00:06<00:00,  8.96it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.31it/s]
                   all          2         62      0.721      0.926      0.932      0.467
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    147/200      3.85G      1.034      1.177      1.076        213        800: 100%|██████████| 60/60 [00:06<00:00,  8.89it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.31it/s]
                   all          2         62      0.793      0.914      0.929      0.473
  0%|          | 0/60 [00:00<?, ?it/s]
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
    148/200      4.54G      1.026      1.105      1.077        326        864: 100%|██████████| 60/60 [00:07<00:00,  8.12it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00, 30.30it/s]
                   all          2         62      0.784      0.938      0.952      0.474
EarlyStopping: Training stopped early as no improvement observed in last 40 epochs. Best results observed at epoch 108, best model saved as best.pt.
To update EarlyStopping(patience=40) pass a new patience value, i.e. `patience=300` or use `patience=0` to disable EarlyStopping.

148 epochs completed in 0.611 hours.
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\weights\last.pt, 5.6MB
Optimizer stripped from C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\weights\best.pt, 5.6MB

Validating C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\weights\best.pt...
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11n summary (fused): 100 layers, 2,672,434 parameters, 0 gradients, 6.8 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  6.05it/s]
                   all          2         62       0.74      0.901      0.952      0.483
           API-Gateway          2          4      0.613          1      0.995      0.298
               Amplify          2          2      0.771          1      0.995      0.497
               Appsync          2          2      0.793          1      0.995      0.427
                Athena          2          2      0.788          1      0.995      0.199
                   CUR          2          2      0.788          1      0.995      0.527
            Cloudfront          2          2      0.771          1      0.995      0.298
             CodeBuild          2          2      0.498          1      0.995      0.697
          CodePipeline          2          2      0.829          1      0.995      0.298
               Cognito          2          2          0          0      0.142     0.0426
                Config          2          2          1      0.841      0.995      0.497
             Dynamo DB          2          2      0.427          1      0.995      0.398
Elastic Container Registry          2          2      0.771          1      0.995      0.796
Elastic Container Service          2          2      0.516          1      0.995      0.398
        Elastic Search          2          2          1          0      0.995      0.796
               Fargate          2          2      0.783          1      0.995      0.398
                 Image          2          2      0.768          1      0.995      0.697
                Lambda          2          8      0.654      0.875      0.867      0.371
               Neptune          2          2      0.995          1      0.995      0.398
        Private Subnet          2          2      0.851          1      0.995      0.597
                    S3          2         10      0.835          1      0.995      0.296
                   SDK          2          2      0.968          1      0.995      0.597
                 Users          2          2      0.807          1      0.995      0.697
                   aws          2          2      0.785          1      0.995      0.895
Speed: 0.3ms preprocess, 71.8ms inference, 0.0ms loss, 1.4ms postprocess per image
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200
🚀 Save dir: C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200
✅ best.pt:  C:\acmattos\dev\tools\Python\ia4devs\runs\detect\yolo11n_custom_200\weights\best.pt
Ultralytics 8.3.144  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 8188MiB)
YOLO11n summary (fused): 100 layers, 2,672,434 parameters, 0 gradients, 6.8 GFLOPs
val: Fast image access  (ping: 0.00.0 ms, read: 138.632.7 MB/s, size: 106.4 KB)
WARNING Box and segment counts should be equal, but got len(segments) = 233, len(boxes) = 426. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
val: Scanning C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\dataset\aws\test\labels.cache... 21 images, 0 backgrounds, 0 corrupt: 100%|██████████| 21/21 [00:00<?, ?it/s]
                                            0% | 0.00/5.39 MB [00:00<?, ?MB/s]: 
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   0%|          | 0/3 [00:00<?, ?it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  33%|███▎      | 1/3 [00:00<00:00,  3.08it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  67%|██████▋   | 2/3 [00:00<00:00,  4.01it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 3/3 [00:00<00:00,  4.35it/s]
                   all         21        426      0.374      0.335      0.327      0.265
                   ACM          1          1          1          0          0          0
                   ALB          5          5      0.152        0.4      0.423      0.369
Active Directory Service          1          1          0          0          0          0
                Athena          1          1      0.786          1      0.995      0.895
                Aurora          4          7          0          0     0.0145    0.00145
          Auto Scaling          4          8       0.23       0.25      0.299      0.206
                   CDN          1          1      0.861          1      0.995      0.796
   Certificate Manager          1          1          0          0          0          0
          Cloud Search          1          1          1          0          0          0
           Cloud Trail          2          3      0.493      0.329      0.312      0.219
           Cloud Watch          5          7       0.27      0.857      0.804      0.731
  CloudFormation Stack          1          1      0.293          1      0.995      0.995
              CloudHSM          1          1          1          0          0          0
            Cloudfront          9          9      0.169      0.222      0.142      0.124
             CodeBuild          1          1      0.562          1      0.995      0.796
            CodeCommit          1          1      0.419          1      0.995      0.895
            CodeDeploy          1          1          1          1      0.995      0.796
               Cognito          1          1          0          0          0          0
                Config          1          6          0          0          0          0
             Container          1          1      0.317          1      0.995      0.697
             Detective          1          1          0          0          0          0
        Direct Connect          4         11      0.829      0.818       0.78      0.525
          Distribution          2          2          0          0          0          0
          Docker Image          1          2          1          0          0          0
             Dynamo DB          8         19      0.574      0.684      0.671      0.536
                   EBS          3          4          1          0      0.213      0.123
                   EC2         13         40      0.377      0.453      0.256      0.175
                   EFS          5          5     0.0592      0.071      0.047     0.0376
      EFS Mount Target          4          9      0.508      0.444      0.353      0.266
                   ELB         10         13       0.36      0.385      0.293      0.213
                   EMR          1          1          0          0          0          0
         Edge Location          1          3          0          0          0          0
           ElastiCache          3          5      0.573        0.4      0.297      0.232
Elastic Container Service          1          2      0.651          1      0.995      0.821
        Elastic Search          1          1          1          0      0.199      0.139
Elemental MediaConvert          1          1        0.5          1      0.995      0.796
Elemental MediaPackage          1          1          0          0          0          0
                 Email          1          1          1          0          0          0
           EventBridge          1          5          1          0          0          0
      Firewall Manager          1          1          0          0          0          0
             Flow logs          1          4          0          0          0          0
               Glacier          1          1          0          0          0          0
                  Glue          1          2      0.623          1      0.995      0.747
             GuardDuty          1          5          1          0          0          0
                   IAM          2          9       0.19      0.111      0.132     0.0846
              IAM Role          2          7      0.166      0.143      0.157     0.0472
              IOT Core          1          1      0.589          1      0.995      0.995
       Inspector Agent          1          1          0          0          0          0
              Internet          7          8      0.447      0.407      0.369      0.296
      Internet Gateway          3          4          0          0     0.0168    0.00337
Key Management Service          2          3          0          0          0          0
  Kinesis Data Streams          2          4      0.287          1      0.995      0.828
                Lambda          4         10      0.378        0.8      0.801       0.69
                 Macie          2          4      0.333       0.25      0.272      0.136
             Memcached          1          2          0          0          0          0
         Mobile Client          1          4      0.464          1      0.995      0.902
           NAT Gateway          4          8          0          0     0.0402     0.0141
      Network Firewall          1          1          0          0          0          0
    Organization Trail          1          4          0          0          0          0
        Private Subnet          3         10          0          0      0.027     0.0102
         Public Subnet          6         18      0.368      0.389      0.227      0.154
                   RDS          6         14      0.223        0.5      0.366      0.296
                 Redis          1          1      0.512          1      0.995      0.796
              Redshift          1          1          1          0      0.995      0.895
                Region          2          2          0          0          0          0
              Route 53          1          1          1          0          0          0
               Route53          9          9      0.274      0.333      0.346        0.3
                    S3         17         24       0.28      0.542      0.414      0.325
                   SDK          1          1      0.227          1      0.995      0.597
                   SES          2          2          0          0          0          0
                   SNS          3          3      0.334      0.667       0.67      0.637
                   SQS          2          2      0.342        0.5      0.253      0.253
             SSM Agent          1          1          0          0          0          0
        Secret Manager          1          1          0          0          0          0
        Security Group          1          1          0          0          0          0
          Security Hub          1          5          1          0          0          0
                Server          4         12      0.175       0.25      0.127     0.0862
                Shield          1          1          1          0          0          0
               Sign-On          1          1          0          0          0          0
              Snowball          1          1          0          0          0          0
         Step Function          1          3      0.789          1      0.995      0.895
       Storage Gateway          1          1          0          0          0          0
       Systems Manager          1          2          1          0          0          0
                 Users         11         13      0.509      0.462      0.325      0.207
            VP Gateway          1          1      0.628          1      0.995      0.796
            VPC Router          2          6      0.503      0.667      0.629       0.51
        VPN Connection          1          1      0.389          1      0.497      0.398
                   WAF          1          1          0          0          0          0
           Web Clients          2          7      0.234      0.143      0.149      0.119
                   aws         11         13      0.454      0.692      0.618      0.435
Speed: 1.4ms preprocess, 24.3ms inference, 0.0ms loss, 1.1ms postprocess per image
Saving C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val\predictions.json...
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\val

🎯 Test Metrics (mean per class):
  Precision:    0.374
  Recall:       0.335
  mAP@0.5:      0.327
  mAP@0.5:0.95: 0.265

image 1/1 C:\acmattos\dev\tools\Python\ia4devs\module_05\05_hackaton\data\sample\aws_01.jpg: 544x640 3 Cloud Watchs, 1 Dynamo DB, 5 Lambdas, 1 S3, 2 SNSs, 2 Userss, 46.3ms
Speed: 2.5ms preprocess, 46.3ms inference, 3.0ms postprocess per image at shape (1, 3, 544, 640)
Results saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict
1 label saved to C:\acmattos\dev\tools\Python\ia4devs\runs\detect\predict\labels
✅ Detailed JSON saved to data\reports\yolo11n_custom_200\results.json
✅ Summary JSON saved to data\reports\yolo11n_custom_200\report.json
[ultralytics.engine.results.Results object with attributes:

boxes: ultralytics.engine.results.Boxes object
keypoints: None
masks: None
names: {0: 'ACM', 1: 'ALB', 2: 'AMI', 3: 'API-Gateway', 4: 'Active Directory Service', 5: 'Airflow_', 6: 'Amplify', 7: 'Analytics Services', 8: 'AppFlow', 9: 'Appsync', 10: 'Athena', 11: 'Aurora', 12: 'Auto Scaling', 13: 'Auto Scaling Group', 14: 'Automated Tests', 15: 'Availability Zone', 16: 'Backup', 17: 'Build Environment', 18: 'CDN', 19: 'CUR', 20: 'Call Metrics', 21: 'Call Recordings', 22: 'Certificate Manager', 23: 'Client', 24: 'Cloud Connector', 25: 'Cloud Map', 26: 'Cloud Search', 27: 'Cloud Trail', 28: 'Cloud Watch', 29: 'CloudFormation Stack', 30: 'CloudHSM', 31: 'CloudWatch Alarm', 32: 'Cloudfront', 33: 'CodeBuild', 34: 'CodeCommit', 35: 'CodeDeploy', 36: 'CodePipeline', 37: 'Cognito', 38: 'Comprehend', 39: 'Config', 40: 'Connect', 41: 'Connect Contact Lens', 42: 'Container', 43: 'Control Tower', 44: 'Customer Gateway', 45: 'DSI', 46: 'Data Pipeline', 47: 'DataSync', 48: 'Deploy Stage', 49: 'Detective', 50: 'Direct Connect', 51: 'Distribution', 52: 'Docker Image', 53: 'Dynamo DB', 54: 'EBS', 55: 'EC2', 56: 'EFS', 57: 'EFS Mount Target', 58: 'EKS', 59: 'ELB', 60: 'EMR', 61: 'Edge Location', 62: 'ElastiCache', 63: 'Elastic Container Registry', 64: 'Elastic Container Service', 65: 'Elastic Search', 66: 'Elemental MediaConvert', 67: 'Elemental MediaPackage', 68: 'Email', 69: 'Endpoint', 70: 'Event Bus', 71: 'EventBridge', 72: 'Experiment Duration', 73: 'Experiments', 74: 'Fargate', 75: 'Fault Injection Simulator', 76: 'Firewall Manager', 77: 'Flask', 78: 'Flow logs', 79: 'GameLift', 80: 'Git', 81: 'Github', 82: 'Glacier', 83: 'Glue', 84: 'Glue DataBrew', 85: 'Grafana', 86: 'GuardDuty', 87: 'IAM', 88: 'IAM Role', 89: 'IOT Core', 90: 'Image', 91: 'Image Builder', 92: 'Ingress', 93: 'Inspector Agent', 94: 'Instances', 95: 'Internet', 96: 'Internet Gateway', 97: 'Jenkins', 98: 'Key Management Service', 99: 'Kibana', 100: 'Kinesis Data Streams', 101: 'Kubernetes', 102: 'Lambda', 103: 'Lex', 104: 'MQ', 105: 'Machine Learning', 106: 'Macie', 107: 'Marketplace', 108: 'Memcached', 109: 'Mobile Client', 110: 'Mongo DB', 111: 'MySQL', 112: 'NAT Gateway', 113: 'Neptune', 114: 'Network Adapter', 115: 'Network Firewall', 116: 'Notebook', 117: 'Order Controller', 118: 'Organization Trail', 119: 'Parameter Store', 120: 'Pinpoint', 121: 'PostgreSQL', 122: 'Private Link', 123: 'Private Subnet', 124: 'Prometheus', 125: 'Public Subnet', 126: 'Quarkus', 127: 'Quicksight', 128: 'RDS', 129: 'React', 130: 'Redis', 131: 'Redshift', 132: 'Region', 133: 'Rekognition', 134: 'Results', 135: 'Route 53', 136: 'Route53', 137: 'S3', 138: 'SAR', 139: 'SDK', 140: 'SES', 141: 'SNS', 142: 'SQS', 143: 'SSM Agent', 144: 'Sagemaker', 145: 'Secret Manager', 146: 'Security Group', 147: 'Security Hub', 148: 'Server', 149: 'Service Catalog', 150: 'Shield', 151: 'Sign-On', 152: 'Slack', 153: 'Snowball', 154: 'Stack', 155: 'Step Function', 156: 'Storage Gateway', 157: 'SwaggerHub', 158: 'Systems Manager', 159: 'TV', 160: 'Table', 161: 'Task Runner', 162: 'Terraform', 163: 'Text File', 164: 'Textract', 165: 'Transcribe', 166: 'Transfer Family', 167: 'Transit Gateway', 168: 'Translate', 169: 'Trusted Advisor', 170: 'Twilio', 171: 'Users', 172: 'VDA', 173: 'VP Gateway', 174: 'VPC Router', 175: 'VPN Connection', 176: 'WAF', 177: 'Web Clients', 178: 'Websites', 179: 'X-Ray', 180: 'aws', 181: 'cache Worker'}
obb: None
orig_img: array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [ 39,  34,  33],
        [ 62,  55,  52],
        [ 54,  45,  42]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 254],
        [235, 228, 225],
        [ 67,  58,  55]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 254],
        [255, 255, 252],
        [ 41,  32,  29]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 248],
        [255, 255, 249],
        [ 49,  43,  36]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 248],
        [247, 239, 232],
        [ 53,  47,  40]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [ 44,  36,  29],
        [ 90,  80,  73],
        [ 51,  43,  36]]], dtype=uint8)
orig_shape: (597, 744)
path: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\module_05\\05_hackaton\\data\\sample\\aws_01.jpg'
probs: None
save_dir: 'C:\\acmattos\\dev\\tools\\Python\\ia4devs\\runs\\detect\\predict'
speed: {'preprocess': 2.4835000513121486, 'inference': 46.330400044098496, 'postprocess': 3.0128000071272254}]
█████████████████████████████████ 100% | 5.39/5.39 MB [00:20<00:00,  3.83s/MB]: 

Process finished with exit code 0
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