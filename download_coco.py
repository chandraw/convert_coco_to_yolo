import os
import requests
import zipfile
import argparse

def download_file(url, filename):
    """Download file from URL with progress bar"""
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    return filename

def extract_zip(zip_path, extract_to):
    """Extract zip file"""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main():
    # Create directories
    os.makedirs('coco2017', exist_ok=True)
    os.makedirs('coco2017/images', exist_ok=True)
    os.makedirs('coco2017/labels', exist_ok=True)
    
    # COCO 2017 dataset URLs
    urls = {
        'train_images': 'http://images.cocodataset.org/zips/train2017.zip',
        'val_images': 'http://images.cocodataset.org/zips/val2017.zip',
        'annotations': 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'
    }
    
    # Download files
    for name, url in urls.items():
        print(f"Downloading {name}...")
        filename = os.path.join('coco2017', f'{name}.zip')
        download_file(url, filename)
        
        # Extract
        print(f"Extracting {name}...")
        if 'images' in name:
            extract_zip(filename, 'coco2017/images/')
        else:
            extract_zip(filename, 'coco2017/')
    
    print("Download completed!")

if __name__ == "__main__":
    main()