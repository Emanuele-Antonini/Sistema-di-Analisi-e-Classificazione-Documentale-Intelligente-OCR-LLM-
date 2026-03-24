
$RequirementsFile = "requirements.txt"
$VenvFolder = "D:\Sistema-di-Analisi-e-Classificazione-Documentale-Intelligente-OCR-LLM-\FastAPI\Intelligence_ocr_llm\.venv"

Write-Host "Initializing virtual environment and installing dependencies" -ForegroundColor Green


Write-Host "Checking if virtual environment folder exists"

if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Python is not installed or not added to PATH."
    Write-Host "Please install Python and ensure it's added to your system's PATH variable." -ForegroundColor Yellow
    exit 1
}


# Definizione del percorso completo a pip.exe all'interno della cartella .venv vrituale

$PipPath = Join-Path -Path $VenvFolder -ChildPath "Scripts\pip.exe"

Write-Host "Installing dependencies from requirements.txt" -ForegroundColor Green
& $PipPath install -r $RequirementsFile


Write-Host "=== Installation Complete ===" -ForegroundColor Green
