from fastapi import FastAPI
from env import SimpleEnv

app = FastAPI()
env = SimpleEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    s, r, d = env.step(action.get("action", "work"))
    return {"state": s, "reward": r, "done": d}

@app.get("/state")
def state():
    return env.state()
