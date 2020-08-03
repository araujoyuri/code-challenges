from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Node:
    label: str
    visited: bool = False

    def mark_visited(self):
        self.visited = True


@dataclass
class Edge:
    destination: Node


class Graph:
    def __init__(self, n: int):
        self.edges = defaultdict(list)
        self.n = n
        self.nodes = {}

    def connect(self, start: int, end: int):
        start_node = Node(start)
        end_node = Node(end)
        start_edge = Edge(start_node)
        end_edge = Edge(end_node)

        self.nodes[start] = start_node
        self.nodes[end] = end_node

        self.edges[start].append(end_edge)
        self.edges[end].append(start_edge)

    def find_all_distances(self, origin: int):
        import queue

        distances = {k: -1 for k in range(self.n)}
        queue = queue.Queue()
        origin = self.nodes[origin]
        distances[origin.label] = 0
        origin.mark_visited()

        queue.put(origin)
        
        while not queue.empty():
            node = queue.get()
            height = distances[node.label]

            for edge in self.edges[node.label]:
                current_node = self.nodes[edge.destination.label]
                if not current_node.visited:
                    distances[current_node.label] = height + 6
                    current_node.mark_visited()
                    queue.put(current_node)
                    edge.destination = current_node

        del distances[origin.label]
        distances = list(distances.values())
        print(" ".join(map(str, distances)))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x-1, y-1)
    s = int(input())
    graph.find_all_distances(s-1)
