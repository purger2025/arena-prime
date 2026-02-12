import os
import uvicorn
from fastapi import FastAPI
# This reaches into your folder to grab the 'Twins' logic
from handleCommand.main import app as neural_forge_app

app = neural_forge_app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
