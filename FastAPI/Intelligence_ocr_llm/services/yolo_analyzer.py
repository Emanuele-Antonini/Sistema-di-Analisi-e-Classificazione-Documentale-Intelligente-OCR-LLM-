import asyncio

from pydantic import BaseModel

from typing import List, Any

import numpy as np

import cv2

from ultralytics import YOLO 

from ultralytics.utils.callbacks import get_default_callbacks
 
# this service implements the model developed by IBM named DocLayNet. It contains a dataset of 8000 document images with 11 classes of layout elements.
# Agisce come un Domain Service

class YoloAnalyzer:

        def __init__(self):

            print("Inizializzazione del tensore YOLOv10x in corso...")
            self.modello = YOLO("D:\\Sistema-di-Analisi-e-Classificazione-Documentale-Intelligente-OCR-LLM-\\FastAPI\\Intelligence_ocr_llm\\models\\yolov10x_best.pt")

        async def analyze(self, dati: List[np.ndarray]) -> List[dict[str, Any]]:
                    
                """
                Analizza un'immagine (array numpy) e restituisce i bounding box rilevati.
                Esegue l'inferenza in un thread separato per non bloccare l'event loop asincrono.
                """
                risultati = await asyncio.to_thread(self.modello.predict, dati, verbose=False)
        
                batch_results = []
                
                # Iteriamo sui risultati, tenendo traccia dell'indice dell'immagine (pagina)
                for page_index, result in enumerate(risultati):
                    page_elements = []
                    
                    # Estraiamo i box per questa specifica pagina
                    for box_data in result.boxes:
                        box_coords = box_data.xyxy[0].cpu().numpy()
                        affidabilita = float(box_data.conf[0].cpu().numpy())
                        id_class = int(box_data.cls[0].cpu().numpy())
                        label = self.modello.names[id_class]
                        
                        element = {
                            "label": label,
                            "affidabilita": round(affidabilita, 4),
                            "x1": int(box_coords[0]),
                            "y1": int(box_coords[1]),
                            "x2": int(box_coords[2]),
                            "y2": int(box_coords[3])
                        }
                        page_elements.append(element)
                    
                    # Strutturiamo l'oggetto finale per mantenere il contesto della pagina
                    batch_results.append({
                        "page_index": page_index,
                        "elements_found": len(page_elements),
                        "elements": page_elements
                    })
                    
                return batch_results
    
    
     

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