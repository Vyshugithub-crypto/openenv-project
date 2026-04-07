class SimpleEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tasks = 5
        self.energy = 10
        return self.state()

    def state(self):
        return {
            "tasks_left": self.tasks,
            "energy": self.energy
        }

    def step(self, action):
        if self.energy <= 0:
            return self.state(), 0, True

        if action == "work":
            self.tasks -= 1
            self.energy -= 2
            reward = 1
        elif action == "rest":
            self.energy += 1
            reward = 0.2
        else:
            reward = -1

        done = self.tasks <= 0
        return self.state(), reward, done