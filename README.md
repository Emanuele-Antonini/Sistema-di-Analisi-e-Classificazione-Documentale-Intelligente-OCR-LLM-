
# Architettura del Sistema di Elaborazione Documentale

Questo progetto implementa una pipeline asincrona ad alte prestazioni per l'analisi dei documenti, unendo l'estrazione in RAM (PyMuPDF), la visione spaziale (YOLOv10x), la lettura ottica (OpenCV + Tesseract) e l'intelligenza semantica (OpenAI GPT-4o-mini).

## Flusso Operativo (Pipeline)

Di seguito è rappresentato il diagramma di sequenza dell'intero iter processuale:

```mermaid
sequenceDiagram
    participant C as Client
    participant R as FastAPI Router
    participant F as ExtractorFactory
    participant Y as YOLO Vision
    participant O as OCRReader
    participant LLM as OpenAI (GPT-4o-mini)

    C->>R: POST /analyze (File Bytes)
    R->>F: extract(bytes)
    F-->>R: List[NumPy Arrays]
    R->>Y: predict(NumPy Arrays)
    Y-->>R: Layout Mapping (BBoxes)
    R->>O: read_text(NumPy Arrays, BBoxes)
    O-->>R: Layout + Text (JSON)
    R->>LLM: async analyze(JSON Payload)
    LLM-->>R: LLMAnalyzerServices Object
''c


# Sistema-di-Analisi-e-Classificazione-Documentale-Intelligente-OCR-LLM-

# L'intera applicazione è stata implementata utilizzando il Service Layer livello di orchestrazione dei casi d'uso, questo modello si 
# interpone esattamente a metà tra l'API web e il modello del dominio.
# Viene implementata la separazione delle responsabilità, l'applicazione FastApi si occupa solo della gestione delle responsabilità legate
# al web.
# Si evitano Test End to End, vengono utlizzati test unitari veloci. Livello di orchestrazione e dei casi d'uso. 
# Domain Service implementa solo la logica core dell'intero progetto. Vengono definiti tutti i casi d'uso dell'applicazione.

<div align="center">
   <h3>🛠️ Tecnologie e Strumenti</h3>
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  
  <img src="https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white" alt="Elasticsearch" />
  
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" />
  
  <img src="https://img.shields.io/badge/OpenAI-000000?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
</p>

  <h3>📫 Trovami su</h3>
  <p>
    <a href="https://www.linkedin.com/in/emanuele-antonini-1592b81a6" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
    </a>
    <a href="INSERISCI_QUI_IL_TUO_LINK_INSTAGRAM" target="_blank">
      <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
    </a>
  </p>

</div>




# Architettura del Sistema di Elaborazione Documentale

Questo progetto implementa una pipeline asincrona ad alte prestazioni per l'analisi dei documenti, unendo l'estrazione in RAM (PyMuPDF), la visione spaziale (YOLOv10x), la lettura ottica (OpenCV + Tesseract) e l'intelligenza semantica (OpenAI GPT-4o-mini).

## Flusso Operativo (Pipeline)

Di seguito è rappresentato il diagramma di sequenza dell'intero iter processuale:

```mermaid
sequenceDiagram
    participant C as Client
    participant R as FastAPI Router
    participant F as ExtractorFactory
    participant Y as YOLO Vision
    participant O as OCRReader
    participant LLM as OpenAI (GPT-4o-mini)

    C->>R: POST /analyze (File Bytes)
    R->>F: extract(bytes)
    F-->>R: List[NumPy Arrays]
    R->>Y: predict(NumPy Arrays)
    Y-->>R: Layout Mapping (BBoxes)
    R->>O: read_text(NumPy Arrays, BBoxes)
    O-->>R: Layout + Text (JSON)
    R->>LLM: async analyze(JSON Payload)
    LLM-->>R: LLMAnalyzerServices Object
