from itertools import permutations
from TSP import TSP

class BruteForce(TSP):
    def __init__(self, points):
        super(BruteForce, self).__init__(points)
        self.l = len(self.points)

    def lengthForPath(self, path):
        length = 0
        ''' Calculating the distance between 2 cities 
                and add it to the total length '''
        for i in range(self.l-1):
            length += self.distance(path[i], path[i+1])
        #close the path
        closeD = self.distance(path[0], path[-1])
        return length + closeD

    def optimise(self):
        if len(self.points) < 2:
            return None, 0
        minLength = float("inf")
        minPath = []
        # Traverse all its permutations, there should be n! permutations
        for path in permutations(self.points):
            ''' calculating the whole length of the current route.
                    The calcalution function should count 
                    the first city as the destination city. '''
            l = self.lengthForPath(path)
            if l < minLength:
                minLength = l
                minPath = list(path)

        # append the first city at the end of route
        minPath.append(minPath[0])
        self.path.extend(minPath)

        # return the route and its total length
        return self.path, self.totalDistance()
