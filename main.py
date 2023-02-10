class Djikstra:
    """Djisktra algorithm"""

    def __init__(self, entry_point, here_i_am, end_point):
        self.entry_point = entry_point
        self.here_i_am = here_i_am
        self.end_point = end_point
        self.graph = {}
        self.visited = []
        self.distance = []
        self.predecessor = []

    def get_sample_dict(self):
        return {
            '0': {'1': 4, '4': 8},
            '1': {'0': 4, '2': 8, '4': 11},
            '2': {'1': 8, '3': 7, '6': 4, '8': 2},
            '3': {'2': 7, '6': 14, '7': 9},
            '4': {'0': 8, '1': 11, '5': 1, '8': 7},
            '5': {'4': 1, '6': 2, '8': 6},
            '6': {'3': 1, '5': 2, '7': 10},
            '7': {'3': 9, '6': 10},
            '8': {'2': 2, '4': 7, '5': 6}
        }

    def set_graph(self, graph: dict):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.distance = [float("inf")] * len(graph)
        self.predecessor = [None] * len(graph)

    def get_graph(self):
        return self.graph

    def get_shortest_path(self):
        self.distance[self.entry_point] = 0

        for i in range(len(self.graph)):
            min_distance = self.get_min_distance_vertex()
            self.visited[min_distance] = True

            for v, w in self.graph[str(min_distance)].items():
                if not self.visited[int(v)] and self.distance[int(v)] > self.distance[min_distance] + w:
                    self.distance[int(v)] = self.distance[min_distance] + w
                    self.predecessor[int(v)] = min_distance

        return self.get_path()

    def get_min_distance_vertex(self):
        min_vertex = float("inf")
        min_index = 0
        for i in range(len(self.distance)):
            if not self.visited[i] and self.distance[i] < min_vertex:
                min_vertex = self.distance[i]
                min_index = i

        return min_index

    def get_path(self):
        path = []
        current = self.end_point
        while current is not None:
            path.append(current)
            current = self.predecessor[current]

        # Reverse the path to get the correct order
        path = path[::-1]

        return path
