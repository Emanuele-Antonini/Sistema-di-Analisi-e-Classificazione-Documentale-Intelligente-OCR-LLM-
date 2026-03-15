import pytest
from services.extractor import PDFDocumentExtractor
import numpy as np
import os
import json
# In questo caso sto implementando il pattern Separation of Concerns per dividere il ruolo di ogni file di test

# pattern architetturale dei test unitari AAA (Arrange, Act, Assert)

@pytest.mark.asyncio

async def test_extraction():

    # Simulazione di un file PDF o immagine da estrarre

    extractor = PDFDocumentExtractor()
    
    percorso_test_pdf = os.path.join("test", "dummy.pdf")
    # with open(percorso_test_pdf, "rb") as file_finto:
    #   pdf_bytes = file_finto.read() # Questo genera la vera byte string
    
    result = extractor.extract(percorso_test_pdf)

    print(json.dumps(result, indent=1))
    
    assert "text" in result  # Verifica che il risultato contenga il testo estratto
    assert isinstance(result["text"], str)  # Verifica che il testo sia una stringa

    #page = result[0]

    #assert isinstance(result["text"], np.ndarray)
    assert len(result["text"]) > 99  
    
    print(" lunghezza maggiore di 3")
    
    # Verifica che l'immagine estratta sia in formato RGB    
    # assert page.shape[2] == 3  # Verifica che l'immagine estratta abbia 3 canali (RGB)


