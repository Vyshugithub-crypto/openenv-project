from fastapi import FastAPI
from env import SimpleEnv
import uvicorn

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

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
