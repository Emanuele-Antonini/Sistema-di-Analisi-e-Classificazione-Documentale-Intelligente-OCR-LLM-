from pydantic import BaseModel

from typing import List

import numpy as np

import cv2

from ultralytics import YOLO 

from ultralytics.utils.callbacks import get_default_callbacks
 
# this service implements the model developed by IBM named DocLayNet. It contains a dataset of 8000 document images with 11 classes of layout elements.

def __init__(self):

    print("Inizializzazione del tensore YOLOv10x in corso...")
    self.modello = YOLO("/models/yolov10x_best.pt")

async def analyze(self, dati: np.ndarray) -> List[dict]:
    
    prediction = self.modello(dati).track()
    
    element_found = []
    
    for r in prediction:
        
          print(r.obb.id) 
          
          print("-----------")
          
          print(r.mask.xy)
         
    for prediction in prediction[0].boxes:
        
        affidabilità = float(prediction.conf[0].cpu().numpy())
        box = prediction.xyxy[0].cpu().numpy()
        bbox_list = prediction.boxes.xyxy.tolist() #boundign boxes all object
        class_list = prediction.boxes.cls.int().tolist() #class index all object
        conf_list = prediction.boxes.conf.tolist() #confidence list all objects
        track_ids = prediction.boxes.id.int().tolist() #track id all objects
        mask_list = prediction.xy 
        
         
        for box, cls, tid ,conf in zip(bbox_list,class_list,conf_list,track_ids):
        
            print(f"Bounding box: {box}, Class index: {cls},"
                   f"Track_id: {tid}, Confidence: {conf},"
                   f"masl_list: {mask_list}")
        
        
        id_class= int(prediction.cls[0].cpu().numpy())
        label = self.modello.names[id_class]
        
        element = {
            "label": label,
            "affidabilità": affidabilità,
            "x1": int(box[0]),
            "y1": int(box[1]),
            "x2": int(box[2]),
            "y2": int(box[3])
        }
        
        element_found.append(element)
      
    return element_found
    
    
     

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