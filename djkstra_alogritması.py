import numpy

sonGraph = numpy.zeros((5, 5))

# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
        print(self.ROW)

    '''Returns true if there is a path from source 's' to sink 't' in residual graph.
    Also fills parent[] to store the path'''

    def BFS(self, s, t, parent):
        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node, then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                    if ind == t:
                        return True

        # We didn't reach the sink in BFS starting from the source, so return false
        return False

    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
        # This array is filled by BFS and to store the path
        parent = [-1] * (self.ROW)
        max_flow = 0  # There is no flow initially

        # Augment the flow while there is a path from the source to the sink
        while self.BFS(source, sink, parent):
            # Find the minimum residual capacity of the edges along the path filled by BFS.
            # Or we can say find the maximum flow through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to the overall flow
            max_flow += path_flow

            # Update residual capacities of the edges and reverse edges along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        i = 0
        while i < self.ROW:
            j = 0
            while j < self.ROW:
                sonGraph[i][j] = self.graph[i][j]
                j += 1
            i += 1

        return max_flow

# Create a graph given in the above diagram
matrix = [[0, 20, 30, 10, 0],
          [0, 0, 40, 0, 30],
          [0, 0, 0, 10, 20],
          [0, 0, 5, 0, 20],
          [0, 0, 0, 0, 0]]

print("--bağlantı-- --akış farkları-- --akış miktarı-- --yön--")

m = 1
x = 0
while x < 5:
    y = 0
    while y < 5:
        if matrix[x][y] > 0:
            matrix[x][y] -= sonGraph[x][y]
            matrix[y][x] -= sonGraph[y][x]
            print(str(m) + ")", " ", (x + 1, y + 1), " ", (matrix[x][y], matrix[y][x]), "-", (matrix[y][x],
                                                                                            matrix[x][y]), "=(",
                  str(matrix[x][y] - matrix[y][x]), ",", str(matrix[y][x] - matrix[x][y]) + ")", " ", str(x
                                                                                                            + 1) + " =>",
                  str(y + 1))
            m += 1
        y += 1
    x += 1

graph = [[0, 20, 30, 10, 0],
         [0, 0, 40, 0, 30],
         [0, 0, 0, 10, 20],
         [0, 0, 5, 0, 20],
         [0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 4

print("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
