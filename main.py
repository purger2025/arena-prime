import os
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="NEURAL_FORGE_SOVEREIGN")

@app.get("/")
def health_check():
    return {
        "status": "active",
        "phase": "HERA",
        "identity": "PURGER2025",
        "neural_forge": "initialized",
        "persona_status": "EDWARD_DOWD_DELETED"
    }

if __name__ == "__main__":
    # Railway dynamic port binding
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
