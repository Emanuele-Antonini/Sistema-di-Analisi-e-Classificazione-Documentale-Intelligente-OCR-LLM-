import pytest
from services.extractor import PDFDocumentExtractor
import numpy as np
import os
import json
# In questo caso sto implementando il pattern Separation of Concerns per dividere il ruolo di ogni file di test

# pattern architetturale dei test unitari AAA (Arrange, Act, Assert)

# The name of test methods must express the function implemented in the logic of the test, and also the variabiles and classes

# It's essential to distinguish between two object: value object and entity object secondo il Domain Driven Design

# Value Object definito esclusivamente dai dati che contine e non possiede un'identità persistente nel tempo, sono tipi immutabili

# Entity è un oggetto che possiede un'identità propria che persiste nel tempo anche se i suoi attributi cambiano, viene identificata da un 
# riferimento unico 
# 
# (ID, matricola, reference)

# Ignorazna della persistenza disaccopiamento 

# I concetti astratti quando si implementa un'applicazione non possono essere incapsulati all'interno di un'etità o di un oggetto valore

# Se è necessario implmentare una funzionalità che coinvolge più ogggetti del dominio si utlizza il pattern Domain Service

# DIP Decoupling tra la logica astratta di funzionamento e infrastruttura tecnica

# TDD garantire correttezza e guidare il design verso la testabilità

# La logica centrale, e perciò il fulcro  del funzionamento dell'applicazione, in questo caso la cartella services deve seguire 
# il principio di "persistence-ignorant", ovvero che non sappia nulla di coeme i dati vengono salvati e in modo tale che si possa 
# effettuare un refactoring aggressivo

# Uno degli obiettivi è l'utilizzo della classe Repository che è un' interfaccia, un'astrazione utilizzata per scollegare 
# l'utilizzo del database che è permanente e persistente dal modello del dominio, e dalle sue classi implementate. Si andrà a 
# creare un adapter che implementa effettivamente le funzionalità di interrogazione del databse.


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


