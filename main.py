from fastapi import FastAPI, Request
import uvicorn
import os

# [IDENTITY: ARENA_PRIME_SERVER]
# [ARCHITECT: THE CAVEMAN]

app = FastAPI()

# --- THE LOGIC CORE (Your Original Code) ---
def orchestrate_command(voice_input):
    cmd = voice_input.lower()
    
    # 1. ROUTE TO AGENT BARON
    if "baron" in cmd:
        return {
            "agent": "BARON",
            "action": "ENTROPY_SCAN",
            "response": "ARCHITECT, I am scanning the game grids for today's entropy spikes. Stand by."
        }
    
    # 2. ROUTE TO THE TWINS
    elif "twins" in cmd or "actuarial" in cmd:
        return {
            "agent": "TWINS",
            "action": "FORENSIC_AUDIT",
            "response": "THE TWINS: Actuarial signals isolated. The +18.2% gap is widening."
        }
    
    # 3. ROUTE TO KERNEL/SYS
    elif "kernel" in cmd or "iterate" in cmd:
        return {
            "agent": "SYS",
            "action": "KERNEL_EXEC",
            "response": "RECONFIGURING SYSTEM CORE... ITERATION SUCCESSFUL."
        }

    # 4. DEFAULT
    else:
        return {
            "agent": "GEMINI",
            "action": "GENERAL_ASSIST",
            "response": "I hear you, Architect. I am coordinating with the cluster."
        }

# --- THE API ENDPOINTS (The Ears) ---

@app.get("/")
def root():
    return {"status": "ONLINE", "message": "ARENA PRIME IS LISTENING."}

@app.get("/root")
def caveman_greeting():
    return {"message": "Hello Caveman the Architect. The Arena is yours."}

@app.post("/command")
async def receive_command(request: Request):
    data = await request.json()
    voice_input = data.get("input", "")
    result = orchestrate_command(voice_input)
    return result

# --- THE LAUNCHER ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
