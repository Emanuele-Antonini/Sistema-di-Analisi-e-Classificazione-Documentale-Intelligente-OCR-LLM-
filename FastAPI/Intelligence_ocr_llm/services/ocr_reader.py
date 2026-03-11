import cv2

import pytesseract

from typing import List




class OCRReader:

    def __init__(self):

        self.modello = pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    async def read_text(self, image_path: str) -> List[dict]: