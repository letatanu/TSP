from TSP import TSP
from copy import deepcopy
class Two_Opt(TSP):
    def __init__(self, points):
        super(Two_Opt, self).__init__(points)
        self.path = deepcopy(points)

    def costChange(self, p1, p2, p3, p4):
        return self.distance(p1, p3) + self.distance(p2,p4) - self.distance(p1, p2) - self.distance(p3, p4)

    def optimise(self):
        if len(self.points) < 2:
            return None, 0
        bestRoute = self.path.copy()
        improved = True
        while improved:
            improved = False
            for i in range(1, len(self.path) - 2):
                for j in range( i+1, len(self.path)):
                    if j-i == 1: continue
                    if self.costChange(bestRoute[i-1], bestRoute[i], bestRoute[j-1], bestRoute[j]) < 0:
                        bestRoute[i:j] = bestRoute[j - 1:i - 1:-1]
                        improved = True
            self.path = bestRoute

        self.path.append(self.path[0])
        return self.path, self.totalDistance()
