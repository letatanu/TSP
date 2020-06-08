import math
import matplotlib.pyplot as plt
from abc import abstractmethod
import numpy as np
from copy import deepcopy
class TSP:
    def __init__(self, points):
        self.points = deepcopy(points)
        self.path = []

    @staticmethod
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    @staticmethod
    def totalLengthOfPath(path):
        totalDistance = 0
        l = len(path)
        for i in range(l - 1):
            totalDistance += TSP.distance(path[i], path[i + 1])
        return totalDistance

    def smallestEdge(self):
        startPoint = None
        endPoint = None
        minLength = float("inf")
        l = len(self.points)
        for i in range(0, len(self.points)):
            for j in range(i+1, l):
                d = TSP.distance(self.points[i], self.points[j])
                if minLength > d:
                    minLength = d
                    startPoint = self.points[i]
                    endPoint = self.points[j]
        return startPoint, endPoint

    def totalDistance(self):
        totalDistance = 0
        l = len(self.path)
        for i in range(l-1):
            totalDistance += self.distance(self.path[i], self.path[i+1])
        return totalDistance

    def plotPath(self, style='bo-', name="TSP"):
        path_ = np.array(self.path)
        plt.plot(path_[:,0], path_[:,1], style)
        plt.axis('scaled')
        plt.axis('off')
        plt.savefig("{}.png".format(name), dpi=800)
        plt.close()

    @abstractmethod
    def optimise(self):
        pass


