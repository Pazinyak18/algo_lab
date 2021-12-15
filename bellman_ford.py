class Graph:

    def __init__(self, verticles):
        self.verticales = verticles

        self.graph = []

    def add_edge(self, vertex, connected_vertex, distance):

        self.graph.append([vertex, connected_vertex, distance])

    def print_solution(self, distance):

        print("Vertex Distance from Source")

        for i in range(self.verticales):
            print("{0}\t\t{1}".format(i, distance[i]))

    def bellman_ford(self, src):

        distances = [float("Inf")] * self.verticales

        distances[src] = 0

        for _ in range(self.verticales - 1):

            for vertex, connected_vertex, distance in self.graph:

                if distances[vertex] != float("Inf") and distances[vertex] + distance < distances[connected_vertex]:
                    distances[connected_vertex] = distances[vertex] + distance

        for vertex, connected_vertex, distance in self.graph:

            if distances[vertex] != float("Inf") and distances[vertex] + distance < distances[connected_vertex]:
                print("Graph contains negative weight cycle")

                return None

        self.print_solution(distances)
        return distances
