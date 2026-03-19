# tests/test_services.py
import pytest
from test.unit.adapter_test import TestAdapter
# from  import UserService

# utilizzo pattern architetturale dei test unitari AAA Arrange Act Assert 

@pytest.mark.asyncio
async def test_activate_user_changes_status_to_active():
    # 1. SETUP: Inizializziamo il nostro ecosistema "Edge-to-Edge"
    # Creiamo il Fake in memoria (il nostro "Edge" di persistenza)[cite: 377, 680].
    fake_repo = TestAdapter()
    
    # Prepopoliamo il fake repo con uno stato iniziale
    await fake_repo.add({"email": "mario@example.com", "status": "pending"})
    
    # Iniettiamo il fake repo nel servizio (il nostro "Edge" di ingresso)[cite: 682, 745].
    service = TestAdapter(repository=fake_repo)

    # 2. AZIONE: Eseguiamo la logica di business
    result = await service.activate_user("mario@example.com")

    # 3. ASSERZIONE: Verifichiamo lo stato finale
    assert result is True
    
    # Controlliamo che il repository rifletta il cambiamento di stato
    # Questo è un test basato sullo stato, tipico del TDD Classico[cite: 728].
    updated_user = await fake_repo.get({"email": "mario@example.com"})
    assert updated_user["status"] == "active"