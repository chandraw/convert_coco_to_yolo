# convert_coco_to_yolo
In a situation for training yolo using a coco dataset, we need a script for converting the COCO Dataset to YOLO format. 

For example, i'm trying to use the COCO2017 dataset.

1. # Create a new conda environment
conda create -n yolo-coco python=3.10 -y #or you may use another version of python

# Activate the environment
conda activate yolo-coco

# Install basic dependencies including the ultralytics-yolo
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
conda install opencv pandas numpy matplotlib tqdm pillow -y
pip install ultralytics albumentations

2. run the download_coco.py . It will download the coco dataset (train2017.zip, val2017.zip, annotations_trainval2017.zip), make some directory (images and labels), then extract the downloaded zip files.
3. download or create coco.yaml and adjust the dataset root dir!
4. run convert_coco_to_yolo.py
5. run train_yolo.py

why i post this? Frustating from the warning when training the yolo:
- (0 images, 118287 backgrounds, 0 corrupt)
- labels are missing or empty in working directory

train: Fast image access ✅ (ping: 0.0±0.0 ms, read: 9586.6±2627.8 MB/s, size: 195.4 KB)
train: Scanning /home/chandra/datasets/coco2017/train2017.cache... 0 images, 118287 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 118287/118287 2.1Git/s 0.0s
WARNING ⚠️ Labels are missing or empty in /home/chandra/datasets/coco2017/train2017.cache, training may not work correctly. See https://docs.ultralytics.com/datasets for dataset formatting guidance.
val: Fast image access ✅ (ping: 0.0±0.0 ms, read: 5708.7±3119.3 MB/s, size: 147.9 KB)
val: Scanning /home/chandra/datasets/coco2017/val2017.cache... 0 images, 5000 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 5000/5000 85.6Mit/s 0.0s
WARNING ⚠️ Labels are missing or empty in /home/chandra/datasets/coco2017/val2017.cache, training may not work correctly. See https://docs.ultralytics.com/datasets for dataset formatting guidance.


Now, after all the script above is executed, we will have complete coco2017 dataset worked for training using yolo model (or models need yolo dataset format as the input).