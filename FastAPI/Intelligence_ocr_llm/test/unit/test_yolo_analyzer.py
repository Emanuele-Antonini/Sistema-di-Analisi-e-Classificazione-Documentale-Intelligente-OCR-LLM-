import pytest
import numpy as np
from services.yolo_analyzer import analyze
from unittest.mock import patch, MagicMock

# In questo caso sto implementando il pattern Separation of Concerns per dividere il ruolo di ogni file di test

# pattern architetturale dei test unitari AAA (Arrange, Act, Assert)

@pytest.mark.asyncio
@patch("services.yolo_analyzer.YOLO")
async def test_yolo(mock_yolo_class):

    # Arrange section
     
    mock_model_instance = MagicMock()
    
    mock_yolo_class.return_value = mock_model_instance
    
    mock_model_instance.names = {0: "Text", 1: "Title"}
    
    mock_result = MagicMock()
    
    mock_result.boxes.id = MagicMock()

    #image = datafactory(height= ,width=)
    
    mock_result.boxes.xyxy.cpu().numpy.return_value = np.array([[50,50,200,150]])
    
    mock_result.boxes.conf.cpu().numpy.return_value = np.array([0.88])

    mock_result.boxes.cls.int().cpu().numpy.return_value = np.array([0])
    
    mock_result.boxes.id.int().cpu().numpy.return_value = np.array([42])
    
    mock_model_instance.track.return_value = [mock_result]
    
    # Act section
    
    dummy_data = np.zeros((640, 640, 3), dtype=np.uint8)
    
    result = await analyze(dummy_data)
    
    # Assert section
   
    assert len(result) == 1
    
    assert result[0]["label"] == "Text"
    
    assert result[0]["affidabilità"] == 0.88
    
    assert result[0]["track_id"] == 42
    
    assert result[0]["x1"] == 50
    
    assert result[0]["x2"] == 50
    
    assert result[0]["y1"] == 200
    
    assert result[0]["y2"] == 150




    
    
