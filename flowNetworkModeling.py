#Source: https://www.programiz.com/dsa/ford-fulkerson-algorithm
from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)

    # Using BFS to search
    def BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def Ford_Fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


graph_normal = [[0, 4, 0, 3, 0, 0], # S
                 [0, 0, 2, 1, 0, 0], # 1
                 [0, 0, 0, 0, 0, 4], # 2
                 [0, 1, 0, 0, 4, 0], # 3
                 [0, 0, 2, 0, 0, 2], # 4
                 [0, 0, 0, 0, 0, 0]] # N

graph_downtime = [[0, 4, 0, 3, 0, 0], # S
                 [0, 0, 2, 1, 0, 0], # 1
                 [0, 0, 0, 0, 0, 1], # 2 --> changed flow
                 [0, 1, 0, 0, 1, 0], # 3 --> changed flow
                 [0, 0, 2, 0, 0, 2], # 4
                 [0, 0, 0, 0, 0, 0]] # N

graph_proposed = [[0, 4, 0, 3, 0, 0], # S
                 [0, 0, 2, 1, 0, 0], # 1
                 [0, 0, 0, 0, 2, 1], # 2 --> changed flow
                 [0, 1, 0, 0, 1, 0], # 3
                 [0, 0, 2, 0, 0, 2], # 4
                 [0, 0, 0, 0, 0, 0]] # N



g_normal = Graph(graph_normal)
g_downtime = Graph(graph_downtime)
g_proposed = Graph(graph_proposed)

print("Max Flow in normal situation: %d" % 
      g_normal.Ford_Fulkerson(source, sink))
print("Max Flow during the downtime: %d" % 
      g_downtime.Ford_Fulkerson(source, sink))
print("Max Flow during downtime in proposed scenario: %d" 
      % g_proposed.Ford_Fulkerson(source, sink))
