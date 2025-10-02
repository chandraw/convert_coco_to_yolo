from ultralytics import YOLO
import os
import torch

def main():
    # Check if GPU is available
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")

    # Load a pre-trained model
    model = YOLO('yolov8n.pt')  

    # Train the model
    results = model.train(
        data='coco.yaml',
        epochs=1,
        imgsz=640,
        batch=16,
        device=device,
        workers=8,
        patience=10,
        save=True,
        save_period=10,
        project='coco2017_training',
        name='yolov8_coco',
        exist_ok=True
    )

    print("Training completed!")

if __name__ == "__main__":
    main()
