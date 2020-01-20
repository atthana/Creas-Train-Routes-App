#########################################################################
###########################Atthana#######################################
#########################################################################
import csv
import  read_csv

class Node():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getName(self):
        return self.name

    def getValue(self):
        return self.value
    

class Routes():

    def __init__(self):
        self.times = []
        self.routes = {}

    def getRoutes(self):
        return self.routes

    def add(self, startNode, stopNode, times):
        if startNode in self.routes:

            self.routes[startNode].append(Node(stopNode, times))
        else:
            self.routes[startNode] = []
            self.routes[startNode].append(Node(stopNode, times))

    def findPaths(self, start, end):
        path = list()
        self.search(start, end, path)
        if(len(path) == 0):
            print("No routes from " + start + " to " + \
                end)
        else:
            for x in path:
                # print(start + "->" + end + x)
                print(x)
            return x

    def search(self, start, end, path, time=0, timeNewNode=0, visited=None, ):

        foundEnd = False

        if start in self.routes:
            if(visited == None):
                visited = list()

            visited.append(start)
            time = time + timeNewNode
            connectedNodes = self.routes[start]
            for x in connectedNodes:
                if(x.getName() == end):

                    foundEnd = True
                    time = time + x.getValue()
                    visited.append(x.getName())
                    break

            if(foundEnd):
                result = "Your trip from " + \
                    start + " to " + end + " includes " + \
                    str(len(visited)-2) + " stops and will take " + str(time) + " minutes."
                visited.clear()
                path.append(result)
                # return (result)
            else:

                for x in connectedNodes:

                    self.search(x.getName(), end, path, time,
                                   x.getValue(), visited)

quizMap = Routes()
csvfile = read_csv.CSV()
csvfile.readcsv()
data = csvfile.getData()

for val in data:
    values = val.split(",")
    quizMap.add(values[0],values[1],int(values[2]))

while True:
    start = input("What station are you getting on the train?: ")
    end = input("What station are you getting off the train?: ")
    quizMap.findPaths(start, end)
    print("==============================================================")
#=========================================================================