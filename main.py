from fastapi import FastAPI
from env import SimpleEnv

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OpenEnv API running"}

env = SimpleEnv()

# ✅ FIXED RESET (POST + no params)
@app.post("/reset")
def reset():
    return env.reset()

# OPTIONAL: also allow GET (extra safe)
@app.get("/reset")
def reset_get():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

# ✅ FIXED STEP (accept JSON body)
from pydantic import BaseModel

class ActionInput(BaseModel):
    action: str

@app.post("/step")
def step(input: ActionInput):
    s, r, d = env.step(input.action)
    return {"state": s, "reward": r, "done": d}

@app.get("/tasks")
def tasks():
    return {
        "tasks": ["easy", "medium", "hard"],
        "actions": ["work", "rest"]
    }

@app.get("/grader")
def grader():
    score = 1.0 if env.tasks <= 0 else 0.5
    return {"score": score}

@app.get("/baseline")
def baseline():
    env.reset()
    total_reward = 0
    for _ in range(10):
        s, r, d = env.step("work")
        total_reward += r
        if d:
            break
    return {"score": total_reward}
