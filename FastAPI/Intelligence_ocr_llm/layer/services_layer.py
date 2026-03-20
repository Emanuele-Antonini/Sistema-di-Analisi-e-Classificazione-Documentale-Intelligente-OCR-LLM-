from db.abastract_db import AbstractRepository
from services.extractor import ExtractorFacotry
from services.yolo_analyzer import YoloAnalyzer
from services.llm import analyzer
from services.ocr_reader import read_text
# Implementendo il pattern Service Layer, la logica della chiamata alle funzionalità di dominio del core e 

# delle interregoazioni al databse di Mongo vengono gestite direttammente da questa astrazione

async def process_and_save_document(file_name: str, file_type: str, file: UploadFile = File(...), repo: AbstractRepository) -> dict:
    
    # 1. Orchestrazione: Estrazione del testo
    
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed."}
       
       raw_byte = await file.read()

    
    try:
        extractor = ExtractorFacotry.create_extractor(file_type)
    except ValueError as e:
        raise ValueError(f"Errore di estrazione: {str(e)}")

    raw_text = extractor.extract(stream=raw_byte, filetype=file_type)

    # 2. Costruzione del documento
    document_data = {
        "nome_file": file_name,
        "tipologia": file_type,
        "testo_estratto": raw_text,
        "stato": "Elaborato"
    }

    # 3. Interazione con il database tramite l'astrazione
    inserted_id = await repo.add(document_data)
    
    return {"id": inserted_id, "file_name": file_name, "status": "success"}


yolo_service = YoloAnalyzer()

async def process_document_layout(file_name: str, image_array: np.ndarray, repo: AbstractRepository) -> Dict[str, Any]:
    """
    Service Layer: Orchestra l'analisi dell'immagine e il salvataggio dei dati.
    """
    # 1. Chiamiamo il servizio di dominio (YOLO)
    try:
        elementi_rilevati = await yolo_service.analyze(image_array)
    except Exception as e:
        raise ValueError(f"Fallimento durante l'inferenza del modello: {str(e)}")

    # 2. Strutturiamo i dati per il nostro sistema
    document_data = {
        "nome_file": file_name,
        "tipologia": "Layout_Documento",
        "elementi_estratti": elementi_rilevati,
        "totale_elementi": len(elementi_rilevati),
        "stato": "Analisi_Completata"
    }

    # 3. Persistenza: salviamo nel database tramite l'astrazione
    inserted_id = await repo.add(document_data)
    
    return {
        "id_record": inserted_id,
        "file_name": file_name,
        "elementi_trovati": len(elementi_rilevati)
    }
     
# Andrò ad implementare varie altre funzionalità come la chiamata get, insert e update dentro il router_api.py