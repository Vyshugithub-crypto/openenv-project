import requests

BASE_URL = "https://vaishnavikongalla-openenv-project.hf.space"

def run():
    print("[START] Running baseline inference")

    # Reset environment
    r = requests.post(f"{BASE_URL}/reset")
    state = r.json()

    total_reward = 0

    for step in range(10):
        print(f"[STEP] {step} state={state}")

        # Always take 'work' action
        r = requests.post(f"{BASE_URL}/step", json={"action": "work"})
        data = r.json()

        state = data["state"]
        reward = data["reward"]
        done = data["done"]

        total_reward += reward

        if done:
            break

    print(f"[END] total_reward={total_reward}")

if __name__ == "__main__":
    run()
