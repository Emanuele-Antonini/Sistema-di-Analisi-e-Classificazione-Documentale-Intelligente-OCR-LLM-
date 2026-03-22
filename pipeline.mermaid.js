sequenceDiagram
    participant C as Client
    participant R as FastAPI Router
    participant F as ExtractorFactory
    participant Y as YOLO Vision
    participant O as OCRReader
    participant LLM as OpenAI (GPT-4o-mini)
    participant DB as MongoDB

    C->>R: POST /analyze (File Bytes)
    R->>F: create_extractor(file_type)
    F-->>R: DocumentExtractor Instance
    R->>F: extract(bytes)
    F-->>R: List[NumPy Arrays]
    
    R->>Y: predict(NumPy Arrays)
    Y-->>R: Layout Mapping (BBoxes)
    
    R->>O: read_text(NumPy Arrays, BBoxes)
    O-->>R: Layout + Text (JSON)
    
    R->>LLM: async analyze(JSON Payload)
    Note over LLM: Enforces Pydantic Schema
    LLM-->>R: LLMAnalyzerServices Object
    
    R->>DB: save(Structured Data)
    R-->>C: 200 OK (Analysis Result)
