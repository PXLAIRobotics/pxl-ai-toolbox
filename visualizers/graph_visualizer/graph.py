import math

class Node:
    def __init__(self, nid, lat, lon):
        self.id = nid
        self.lat = float(lat)
        self.lon = float(lon)
        self.x = float(lon)
        self.y = float(lat)
        self.costs = {}

    def addCost(self, toNodeId, cost):
        self.costs[toNodeId] = cost

    def dist(self, other):
        return math.sqrt(math.pow((self.x-other.x), 2) + math.pow((self.y-other.y), 2))

class Graph:
    def __init__(self):
        self.nodes = {}
        self.nodeArray = []

    def addNode(self, nid, node):
        self.nodes[nid] = node
        self.nodeArray.append(node)

    def addEdge(self, fromNodeId, toNodeId):
        self.nodes[fromNodeId].addCost(toNodeId, self.cost(fromNodeId, toNodeId))

    def cost(self, fromNodeId, toNodeId):
        fromNode = self.nodes[fromNodeId]
        toNode = self.nodes[toNodeId]
        return fromNode.dist(toNode)

    def status(self):
        print("Got " + str(len(self.nodes)) + " nodes")

