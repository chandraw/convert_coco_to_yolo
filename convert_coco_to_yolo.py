import os
import json
from tqdm import tqdm
import argparse

def convert_coco_to_yolo(coco_json_path, output_dir, images_dir):
    """Convert COCO annotations to YOLO format"""

    # Load COCO annotations
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # Create mapping from image id to image info
    images = {img['id']: img for img in coco_data['images']}

    # Create mapping from category id to category name
    categories = {cat['id']: cat for cat in coco_data['categories']}

    # Group annotations by image id
    annotations_by_image = {}
    for ann in coco_data['annotations']:
        img_id = ann['image_id']
        if img_id not in annotations_by_image:
            annotations_by_image[img_id] = []
        annotations_by_image[img_id].append(ann)

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Convert each image's annotations
    for img_id, annotations in tqdm(annotations_by_image.items()):
        img_info = images[img_id]
        img_width = img_info['width']
        img_height = img_info['height']
        img_filename = img_info['file_name'].replace('.jpg', '.txt')

        # Create YOLO format file
        yolo_lines = []
        for ann in annotations:
            # Get category ID (YOLO uses 0-indexed class IDs)
            category_id = ann['category_id'] - 1  # COCO starts at 1, YOLO at 0

            # Convert bbox from [x, y, width, height] to [x_center, y_center, width, height] normalized
            bbox = ann['bbox']
            x_center = (bbox[0] + bbox[2] / 2) / img_width
            y_center = (bbox[1] + bbox[3] / 2) / img_height
            width = bbox[2] / img_width
            height = bbox[3] / img_height

            yolo_lines.append(f"{category_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

        # Write to file
        output_path = os.path.join(output_dir, img_filename)
        with open(output_path, 'w') as f:
            f.write('\n'.join(yolo_lines))

def main():
    # Convert training annotations
    print("Converting training annotations...")
    convert_coco_to_yolo(
        'annotations/instances_train2017.json',
        'labels/train2017',
        'images/train2017'
    )

    # Convert validation annotations
    print("Converting validation annotations...")
    convert_coco_to_yolo(
        'annotations/instances_val2017.json',
        'labels/val2017',
        'images/val2017'
    )

    print("Conversion completed!")

if __name__ == "__main__":
    main()
