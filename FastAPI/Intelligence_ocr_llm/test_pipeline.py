import cv2
import asyncio
import numpy as np
from services.yolo_analyzer import YoloAnalyzer
from services.extractor import ExtractorFactory
from services.ocr_reader import OCRReader
from services.llm import LLMAnalyzer
from pathlib import Path
from typing import List

async def analyze_documents(file_path: str, type_file: str):
    
   print(f"Analisi del documento: {file_path} di tipo {type_file} in corso...")
      
   factory = ExtractorFactory()
   extractor = factory.create_extractor(type_file)

   yolo = YoloAnalyzer() 
   llm_analyzer = LLMAnalyzer(api_key)
                              
   #with open (file_path, "rb") as file_list:
        
   documents = Path(file_path)

   file_buffer = []

   for document in documents.glob("*.jpg"):

      with open(document, "rb") as file:
         
        file_buffer.append(file.read())    # devo iterare su più file che poi verranno estratti all'interno di extract_batch

   print(f"file_buffer_ {len(file_buffer)} properties: {[type(fb) for fb in file_buffer]} Type List: {type(file_buffer)}")

   data = []
   
   print("Content:", file_buffer[0][:100])  # Stampa i primi 100 byte del primo file per verifica
   print("Content:", file_buffer[1][:100])  # Stampa i primi 100 byte del secondo file per verifica
   
   for i in range(len(file_buffer)):

     estraction = extractor.extract_batch([file_buffer[i]])  # estraggo un file alla volta per testare la pipeline, in futuro potrei estrarre più file contemporaneamente
     data.append(estraction)

   immagini_per_yolo = []

   for risultato in data:
    # risultato[0] accede al dizionario
     pagine = risultato[0]["extracted_data"]
     immagini_per_yolo.extend(pagine)

   print(f"{len(data)} YOLOv10x... Type data: {[type(d) for d in data]}")

   print("YoLOv10x analysis phase...")
   
   # Crea una lista di "task" (promesse di esecuzione) senza parentesi quadre extra
   #tasks = [yolo.analyze(pagine_documento) for pagine_documento in data]

   # Esegue tutte le analisi YOLO in parallelo e attende che finiscano tutte
   #tutti_i_risultati_yolo = await asyncio.gather(*tasks)

   yolo_results = []

   ocr_reader = OCRReader()

    # Iteriamo direttamente sulla lista delle 29 immagini
   for page_index, immagine_originale in enumerate(immagini_per_yolo):
        
        print(f"\n--- Elaborazione Pagina {page_index + 1} di {len(immagini_per_yolo)} ---")
        
        # 1. INFERENZA: Passiamo la singola immagine racchiusa in una lista
        risultato_corrente = await yolo.analyze([immagine_originale])
        
        # Poiché abbiamo passato 1 sola immagine, estraiamo l'unico risultato restituito
        risultato_pagina = risultato_corrente[0]
        yolo_results.append(risultato_pagina)
        
        # 2. PREPARAZIONE VISIVA: OpenCV usa BGR, convertiamo l'immagine originale
        immagine_bgr = cv2.cvtColor(immagine_originale.copy(), cv2.COLOR_RGB2BGR)
        
        elementi_trovati = risultato_pagina["elements"]
        print(f"Trovati {len(elementi_trovati)} elementi.")
        
        # 3. DISEGNO: Tracciamo i bounding box
        for elemento in elementi_trovati:
            x1, y1, x2, y2 = elemento["x1"], elemento["y1"], elemento["x2"], elemento["y2"]
            label = elemento["label"]
            conf = elemento["affidabilita"]
            
            print(f"   - {label} ({conf*100:.1f}%): [{x1}, {y1}, {x2}, {y2}]")
            
            # Disegna il rettangolo verde
            cv2.rectangle(immagine_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Aggiungi l'etichetta di testo sopra il rettangolo
            cv2.putText(immagine_bgr, f"{label} {conf:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # 4. VISUALIZZAZIONE A SCHERMO
        nome_finestra = f"Risultato YOLO - Pagina {page_index + 1}"
        cv2.imshow(nome_finestra, immagine_bgr)
        
        # Mette in pausa il ciclo: attende che tu prema un tasto (es. la barra spaziatrice)
        # NOTA: Clicca sull'immagine, non sul terminale, prima di premere il tasto!
        cv2.waitKey(0) 
        
        # Chiude la finestra corrente prima di passare alla pagina successiva
        cv2.destroyWindow(nome_finestra)
        
        result = await ocr_reader.read_text(immagine_bgr, risultato_corrente[0]["elements"])
        
        for elemento in result:
                #etichetta = elemento["label"]
                #testo = elemento["testo_estratto"]
                
                # Stampiamo solo se Tesseract ha effettivamente trovato del testo
                #if testo: 
                    print(f"{elemento}")

        print("\nAnalisi e visualizzazione di tutte le pagine completata!")

        llm_result = await llm_analyzer.analyze(result)

        #analyze(,)

        print(f"\n-- Result for page {llm_result}")


if __name__ == "__main__":
   
   FILE= "D:\\Sistema-di-Analisi-e-Classificazione-Documentale-Intelligente-OCR-LLM-\\FastAPI\\test\\images"   # percorso del file da analizzare

   TYPE= "jpg"

   asyncio.run(analyze_documents(FILE, TYPE))
    


