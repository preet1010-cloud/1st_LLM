# 1st_LLM
This is my 1st deployment of an LLM model using Ollama

Build, Pull the Model, and Launch:-

Build and start the containers in the background:
PowerShell
"docker compose up -d --build"

Download the qwen2.5:1.5b model inside the running Ollama container (equivalent to vLLM downloading the Hugging Face weights):
PowerShell
"docker exec -it ollama-backend ollama pull qwen2.5:1.5b"

(Wait for the download bar to hit 100%—this model is ~1 GB).
Verify the API endpoint (just like checking /v1/models in the video):
PowerShell
"curl http://localhost:11434/v1/models"

