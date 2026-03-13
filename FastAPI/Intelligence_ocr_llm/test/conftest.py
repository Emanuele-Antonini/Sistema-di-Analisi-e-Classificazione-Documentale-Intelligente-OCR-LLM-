# In ragione del fatto che i servizi LLMAnalyzer e YoloAnalyzer sono componeneti chiave del sistema, è fondamentale garantire che funzionino correttamente

# Si  evita di verificarne il funzionamento solo tramite il test con l'interfaccia GUI della libreria di FastAPI, ma diffatti si implementano dei test unitari
# specifci implementando la libreria python test e assicurandosi che la progettazione e l'architettazione del codice siano modulari e rispettino i principi 
# SOLID e GOF.

# implementiamo in questo caso il pattern Simple Factory pattern creazionale, questo perché è necessario chiamare il metodo implementato in questo file
# all'interno delle classi di test, in talm modo verrà effettuato un solo istanziamento quando necessario, e verrà, pertanto, impostata una logica di 
# istanziazione centralizzata, di oggetti complessi.

import pytest

import numpy as np

# Implemento la classe per la generazione dei documenti di test, e per la traduzione in raw byte del pdf dummy.

class DataFactory:

  @staticmethod
  
  def generatedata(altezza=800, larghezza=600):

    # Genera una finta pagina PDF rasterizzata (matrice NumPy RGB)

    return np.zeros((altezza, larghezza, 3), dtype=np.uint8) 


# Utilizzando questo blocco: @pytest.fixture si implementa il pattern Injection Dependency

@pytest.fixture

def datafactory():

    return DataFactory()