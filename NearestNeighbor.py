from TSP import TSP
import math

class NearestNeighbor(TSP):
    def __init__(self, points):
        super(NearestNeighbor, self).__init__(points)
        #initialize the start city is the first point.
        startPoint = self.points[0]
        self.points.remove(startPoint)
        self.path = [startPoint]

    '''This function is to get the nearest neighbor,
    which is not in the current route, of
    the current node'''
    def closestPoint(self):
        dMin = float("inf")
        currentPoint = self.path[-1]
        closestPoint = None
        for p in self.points:
            d = self.distance(p,currentPoint)
            if dMin > d:
                dMin = d
                closestPoint = p
        return closestPoint, dMin

    '''run NN on the given set of nodes '''
    def optimise(self):
        if len(self.points) < 2:
            return None, 0
        while len(self.points) > 0 :
            closestPoint, d = self.closestPoint()
            # append the found node to the route
            self.path.append(closestPoint)
            # in meanwhile, remove the found point from the given set
            self.points.remove(closestPoint)

        # closing the path
        self.path.append(self.path[0])

        # return the route and its total length
        return self.path, self.totalDistance()