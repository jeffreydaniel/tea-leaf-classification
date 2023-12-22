from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2

model=YOLO("path to model.pt")

results=model.predict(source=0,show=True)