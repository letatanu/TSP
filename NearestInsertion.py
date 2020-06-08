from TSP import TSP
import numpy as np
class NearestInsertion(TSP):
    def __init__(self, points):
        super(NearestInsertion, self).__init__(points)
        # initialize the route by random node in the set
        # also remove it from the set
        startPoint = self.points[np.random.randint(len(self.points))]
        self.points.remove(startPoint)
        self.path = [startPoint]

    '''This function is to get the nearest neighbor 
    to the current path'''
    def closestPoint(self):
        minLength = float("inf")
        closestPoint = None
        for inPoint in self.path:
            for outPoint in self.points:
                d = self.distance(inPoint, outPoint)
                if  d < minLength:
                    minLength = d
                    closestPoint = outPoint

        # return the length and closestPoint
        return minLength, closestPoint

    '''This function to find the 
    most proper location to insert the found node
    to the current route'''
    def insertNodeToPath(self, insertNode):
        minLength = float("inf")
        insert = 0
        l = len(self.path)
        for i in range(l):
            tmpPath = self.path.copy()
            # make a try to insert the insertNode
            tmpPath.insert(i, insertNode)
            # make closed route
            tmpPath.append(tmpPath[0])
            d = self.totalLengthOfPath(tmpPath)
            if d < minLength:
                minLength = d
                insert = i

        # return the insertion location
        return insert

    def optimise(self):
        totalDistance = 0
        # run until there is no nodes left in the given set.
        while len(self.points) > 0:
            # find the nearest node to the route
            d, closestPoint = self.closestPoint()
            # find the most proper location to insert the found point
            idInsert = self.insertNodeToPath(closestPoint)
            # insert it to the route and remove it from the given set.
            self.path.insert(idInsert, closestPoint)
            self.points.remove(closestPoint)
            totalDistance += d

        self.path.append(self.path[0])
        return self.path, self.totalDistance()


