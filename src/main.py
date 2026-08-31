import cv2
import json
import csv
import os
from easyocr import Reader
import numpy as np
from config import *
from parser import parse_scoreboard

print("Starting Cricket Scoreboard Extractor...")

os.makedirs("outputs", exist_ok=True)

reader = Reader(['en'], gpu=False)
cap = cv2.VideoCapture(VIDEO_PATH)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Video: {frame_count} frames, {fps} FPS")

results = []
x1, y1, x2, y2 = ROI

for i in range(0, min(frame_count, 200), FRAME_SAMPLE_RATE):  # First 200 frames
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    if not ret:
        continue
    
    roi = frame[y1:y2, x1:x2]
    result = reader.readtext(roi)
    
    if result:
        text = ' '.join([item[1] for item in result])
        conf = np.mean([item[2] for item in result])
        
        if conf > OCR_CONFIDENCE_THRESHOLD:
            parsed = parse_scoreboard(text)
            results.append({
                'frame': i,
                'text': text,
                'confidence': float(conf),
                'parsed': parsed
            })
            print(f"Frame {i}: {text[:80]}... ({conf:.2f})")

cap.release()

with open('outputs/results.json', 'w') as f:
    json.dump(results, f, indent=2)

with open('outputs/results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['frame', 'text', 'confidence', 'parsed'])
    for r in results:
        writer.writerow([r['frame'], r['text'], r['confidence'], r['parsed']])

print(f"\nDone! {len(results)} frames processed")
print("Results saved to outputs/")