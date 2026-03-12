import pytest
from services.extractor import ImageDocumentExtractor
import numpy as np

@pytest.mark.asyncio

async def test_extraction():

    # Simulazione di un file PDF o immagine da estrarre
    file_path = "test_document.pdf"  # Sostituisci con un percorso reale o un mock

    extractor = ImageDocumentExtractor()
    result = extractor.extract(file_path)

    assert "text" in result  # Verifica che il risultato contenga il testo estratto
    assert isinstance(result["text"], str)  # Verifica che il testo sia una stringa

    page = result[0]

    assert isinstance(page, np.ndarray)
    assert page.ndim == 3  # Verifica che l'immagine estratta sia in formato RGB    
    assert page.shape[2] == 3  # Verifica che l'immagine estratta abbia 3 canali (RGB)


