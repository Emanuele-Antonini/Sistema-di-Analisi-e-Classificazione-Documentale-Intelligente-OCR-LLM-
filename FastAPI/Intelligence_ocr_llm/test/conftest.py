# In ragione del fatto che i servizi LLMAnalyzer e YoloAnalyzer sono componeneti chiave del sistema, è fondamentale garantire che funzionino correttamente

# Si  evita di verificarne il funzionamento solo tramite il test con l'interfaccia GUI della libreria di FastAPI, ma diffatti si implementano dei test unitari
# specifci implementando la libreria python test e assicurandosi che la progettazione e l'architettazione del codice siano modulari e rispettino i principi 
# SOLID e GOF.

import pytest
from services.extractor import ImageDocumentExtractor
import numpy as np

@pytest.mark.asyncio

async def test_extraction(data):

    # Simulazione di un file PDF o immagine da estrarre
    file_path = "test_document.pdf"  # Sostituisci con un percorso reale o un mock

    extractor = ImageDocumentExtractor()

    result = await extractor.extract(file_path)

    assert "text" in result  # Verifica che il risultato contenga il testo estratto
    assert isinstance(result["text"], str)  # Verifica che il testo sia una stringa
    assert len(result) > 0  # Verifica che il testo estratto non sia vuoto