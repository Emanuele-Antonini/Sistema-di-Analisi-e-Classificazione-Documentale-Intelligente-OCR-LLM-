from abc import ABC, abstractmethod
import fitz
import numpy as np
from typing import List, Dict, Any

# Interfaccia unificata per la strategia
class DocumentExtractor(ABC):
    @abstractmethod
    def extract_batch(self, file_buffers: List[bytes]) -> List[Dict[str, Any]]:
        """
        Elabora una lista di documenti in formato byte e restituisce i dati estratti.
        L'output è standardizzato in una lista di dizionari.
        """
        pass

class PDFDocumentExtractor(DocumentExtractor):
    def extract_batch(self, file_buffers: List[bytes]) -> List[Dict[str, Any]]:
        results = []
        
        for buffer in file_buffers:
            # Usiamo 'with' (Context Manager) per chiudere automaticamente il documento e liberare la RAM
            with fitz.open(stream=buffer, filetype="pdf") as document:
                # Estrazione rapida del testo usando list comprehension
                text = "".join([page.get_text() for page in document])
                results.append({
                    "status": "success",
                    "type": "pdf", 
                    "extracted_data": text
                })
                
        return results
    

class ImageDocumentExtractor(DocumentExtractor):
    def extract_batch(self, file_buffers: List[bytes]) -> List[Dict[str, Any]]:
        results = []
        
        for buffer in file_buffers:
            image_extracted = []
            
            # Apertura del buffer in RAM. Nota: filetype="png" indica a fitz come interpretare il flusso stream
            with fitz.open(stream=buffer, filetype="png") as document:
                for page in document:
                    matrix = fitz.Matrix(2, 2)
                    pix_map = page.get_pixmap(matrix=matrix, alpha=False)
                    
                    # Creazione dell'array NumPy
                    image_matrix_rgb = np.frombuffer(
                        pix_map.samples, 
                        dtype=np.uint8
                    ).reshape(pix_map.h, pix_map.w, pix_map.n)
                    
                    image_extracted.append(image_matrix_rgb)
            
            results.append({
                "status": "success",
                "type": "image", 
                "extracted_data": image_extracted
            })
            
        return results
    

class ExtractorFactory:
    @staticmethod
    def create_extractor(file_type: str) -> DocumentExtractor:
        # Normalizziamo la stringa in minuscolo per evitare errori di case-sensitivity
        file_type = file_type.lower()
        
        if file_type == "pdf":
            return PDFDocumentExtractor()
        elif file_type in ["jpg", "jpeg", "png"]:
            return ImageDocumentExtractor()
        else:
            raise ValueError(f"Formato file non supportato: {file_type}")