from pydantic import BaseModel, Field

from openai import AsyncOpenAI

import json

class LLMAnalyzerServices(BaseModel):

    categoria: str = Field(description="")
    sommario: str = Field(description="")
    entity_key : list[str] = Field(description="")
    lingua: str = Field(description="")
    warning : bool = Field(description="")
 
#  
# Implementiamo il cervello dell'analizzatore LLM
#

class LLMAnalyzer:

    def __init__ (self, api_key: str):

        self.client = AsyncOpenAI(api_key=api_key)

        self.modello = "gpt-4o-mini" # Viene introdotto il modello da utilizzare per l'analisi

# -> LLMAnalyzerServices: a livello sintattico rappresenta il 'returtn type Hint', stai firmando un Contratto Visivo e Strutturale, di modo che 
# chiunque utilizzi questo metodo sa esattamente cosa aspettarsi in uscita, e può contare su una struttura dati ben definita, con campi specifici 
# come 'categoria' e 'sommario', che rappresentano le informazioni chiave restituite dall'analisi LLM. Questo rende il codice più leggibile, 
# manutenibile e facilita l'integrazione con altre parti del sistema che si aspettano un output strutturato.

  async def analyze(self, data_ocr: dict) -> LLMAnalyzerServices:
     
      system_prompt = ("Sei un analista documentale esperto. Il tuo compito è ricevere il testo "
            "estratto da un sistema OCR (organizzato in blocchi spaziali da YOLO) "
            "e comprenderne il significato profondo. "
            "Estrai le informazioni richieste attenendoti rigorosamente ai fatti presenti nel testo.")

      dati_input_str = json.dumps(data_ocr, indent=2)
   
      result = await self.client.beta.chat.completions.parse(model=self.modello,
                                                       messages=[
                                                           { "role:" "system", "content": system_prompt},
                                                           {  "role": "user", "content": f"Ecco i dati estratti dal documento:\n\n{dati_input_str}"} 
                                                           ],
                                                       response_format=LLMAnalyzerServices)

      structure = result.choices[0].message.parsed

      return structure