from pydantic import BaseModel, Field

from openai import AsyncOpenAI

import json

class LLMAnalyzerServices(BaseModel):

    categoria: str = Field()
    sommario: str = Field()

 
#  
# Implementiamo il cervello dell'analizzatore LLM
#

class LLMAnalyzer:

    def __init__ (self, api_key: str):

        self.client = AsyncOpenAI(api_key=api_key)

        self.modello = "" # Viene introdotto il modello da utilizzare per l'analisi

# -> LLMAnalyzerServices: a livello sintattico rappresenta il 'returtn type Hint', stai firmando un Contratto Visivo e Strutturale, di modo che 
# chiunque utilizzi questo metodo sa esattamente cosa aspettarsi in uscita, e può contare su una struttura dati ben definita, con campi specifici 
# come 'categoria' e 'sommario', che rappresentano le informazioni chiave restituite dall'analisi LLM. Questo rende il codice più leggibile, 
# manutenibile e facilita l'integrazione con altre parti del sistema che si aspettano un output strutturato.

async def analyze(self, data_ocr: dict) -> LLMAnalyzerServices:



   

    result = client.chat.completions

    return result