from fastapi import FastAPI
from env import SimpleEnv

app = FastAPI()
env = SimpleEnv()

@app.get("/reset")
def reset():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

@app.post("/step")
def step(action: str):
    s, r, d = env.step(action)
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