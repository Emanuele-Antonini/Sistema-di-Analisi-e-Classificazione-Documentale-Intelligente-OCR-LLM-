from abc import ABC, abstractmethod

import fitz

import numpy as np

# This code defines an abstract base class called DocumentExtractor which allow to implement different document extraction methods.
# It implemnts the pattenr GOF Strategy, which allows to define a family of method and algorithms, encapsulate each of them and make 
# them interchangeable.

class DocumentExtractor(ABC):
    @abstractmethod
    def extract(self, file_path: str) -> dict:
        pass


class PDFDocumentExtractor(DocumentExtractor):
    def extract(self, file_path: str) -> dict:
        # Implementation of text xtraction from a PDF using PyMuPDF
        document = fitz.open(file_path)
        text = ""
        for page in document:
            text += page.get_text()
        return {"text": text}
    

class ImageDocumentExtractor(DocumentExtractor):
    def extract(self, content_byte: bytes):

        image_extracted = []

        document = fitz.open(content_byte, filetype="png")

        for page in range(len(document)):
            
           pagina= document.load_page(page)

           matrix = fitz.Matrix(2,2)

           pix_map = pagina.get_pixmap(matrix=matrix, alpha=False)

           image_matrix_rgb = np.frombuffer(pix_map.samples, dtype=np.uint8).reshape(pix_map.h, pix_map.w, pix_map.n)

           image_extracted.append(image_matrix_rgb)
           
           #image_in_byte = pix_map.tobytes("png")

           #image_extracted.append(image_in_byte)

        document = fitz.close()

        return  image_extracted
    

class ExtractorFacotry:
    @staticmethod
    def create_extractor(file_type: str) -> DocumentExtractor:
        if file_type == "pdf":
            return PDFDocumentExtractor()
        elif file_type in ["jpg", "jpeg", "png"]:
            return ImageDocumentExtractor()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

