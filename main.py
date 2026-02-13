
# Routes voice-to-text commands to the specific Agent Cluster

def orchestrate_command(voice_input):
    cmd = voice_input.lower()
    
    # 1. ROUTE TO AGENT BARON (Games/Entropy/Strategy)
    if "baron" in cmd:
        return {
            "agent": "BARON",
            "action": "ENTROPY_SCAN",
            "response": "ARCHITECT, I am scanning the game grids for today's entropy spikes. Stand by."
        }
    
    # 2. ROUTE TO THE TWINS (Forensics/Actuarial/Hera)
    elif "twins" in cmd or "actuarial" in cmd:
        return {
            "agent": "TWINS",
            "action": "FORENSIC_AUDIT",
            "response": "THE TWINS: Actuarial signals isolated. The +18.2% gap is widening."
        }
    
    # 3. ROUTE TO KERNEL/SYS (System Iterations/Builds)
    elif "kernel" in cmd or "iterate" in cmd:
        return {
            "agent": "SYS",
            "action": "KERNEL_EXEC",
            "response": "RECONFIGURING SYSTEM CORE... ITERATION SUCCESSFUL."
        }

    # 4. DEFAULT (GEMINI/SOVEREIGN BRIDGE)
    else:
        return {
            "agent": "GEMINI",
            "action": "GENERAL_ASSIST",
            "response": "I hear you, Architect. I am coordinating with the cluster."
        }
