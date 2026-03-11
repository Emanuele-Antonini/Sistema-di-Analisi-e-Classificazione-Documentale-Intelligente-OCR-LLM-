from pydantic import BaseModel

from typing import List

import numpy as np

import cv2

from ultralytics import YOLO 

from ultralytics.utils.callbacks import get_default_callbacks
 
# this service implements the model developed by IBM named DocLayNet. It contains a dataset of 8000 document images with 11 classes of layout elements.

def __init__(self):

    self.modello = YOLO("/models/yolov10x_best.pt")

async def 

# model = YOLO("yolo26n.yaml")

# model.train(data="C:\Users\emanuele.antonini\Documents\Sistema-di-Analisi-e-Classificazione-Documentale-Intelligente-OCR-LLM-\Garbage Detection.v8i.yolov8\data.yaml", epochs=50)

# metrics = model.val()

# print("--- RISULTATI DELLA VALIDAZIONE ---")
# print(f"Precisione (Precision): {metrics.box.mp}")
# print(f"Richiamo (Recall): {metrics.box.mr}")
# print(f"mAP a 50 (Mean average Precision): {metrics.box.map50}")
# print(f"mAP complessivo (50-95): {metrics.box.map}")
#callbacks = get_default_callbacks()
#for nomemetodo in callbacks.keys():
# print(nomemetodo)


#def predict_callback_example(predictor):
    
#    print(f"...Callbacks logs...\n"
#          f"model prediction started .....\n"
#          f"prediction results: {predictor.results}...\n")
    
    
    
#model.add_callback("on_predict_postprocess_end", predict_callback_example)
#model.predict(source = 0)