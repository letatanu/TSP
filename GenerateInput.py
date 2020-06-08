import numpy as np
class InputGenerator:
    def __init__(self, size, maxX, maxY):
        self.size = size
        self.maxX = maxX
        self.maxY = maxY

    def generate(self):
        return  [(x,y) for (x,y) in zip(np.random.choice(self.maxX, size=(self.size,), replace=False), np.random.choice(self.maxY, size=(self.size,), replace=False))]
