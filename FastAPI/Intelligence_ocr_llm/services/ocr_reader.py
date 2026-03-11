import cv2

import pytesseract

from typing import List

class OCRReader:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        self.configurazione_tesseract = r'--oem 3 --psm 6'


    async def read_text(self, image, layout_yolo: List[dict]) -> List[dict]:

       result = []

       for element in layout_yolo:
          
           x1, y1, x2, y2 = element['x1'],element['y1'],element['x2'],element['y2']

           image_cropped = image[y1:y2, x1:x2]
       
           ritaglio_grigio = cv2.cvtColor(image_cropped, cv2.COLOR_BGR2RGB)

           testo_letto = pytesseract.image_to_string(
                ritaglio_grigio, 
                config=self.configurazione_tesseract
            )

           testo_letto_ = testo_letto.strip()

           result.append(testo_letto_)

       return result