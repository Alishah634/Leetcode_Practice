print(f'''2642. Design Graph With Shortest Path Calculator
Hard
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:
Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.

Example 1:
Input
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output
[null, 6, -1, null, 6]

Explanation
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.
 

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1)
edges[i].length == edge.length == 3
0 <= fromi, toi, from, to, node1, node2 <= n - 1
1 <= edgeCosti, edgeCost <= 106
There are no repeated edges and no self-loops in the graph at any point.
At most 100 calls will be made for addEdge.
At most 100 calls will be made for shortestPath.
''')

import heapq, termcolor
class Graph:
    
    def __init__(self, n, edges):
        self.adjacencyList = [[] for _ in range(n)]
        for edge in edges:
            self.adjacencyList[edge[0]].append((edge[1],edge[2]))
    
    def addEdge(self, edge) -> None:
        self.adjacencyList[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstra(node1, node2)
    
    # Dijkstra's algorithm to find the shortest path
    def dijkstra(self, start: int, end: int) -> int:
        n = len(self.adjacencyList)
        distances = [float('inf')] * n
        distances[start] = 0
        # Priority queue to efficiently retrieve the node with the minimum distance
        priorityQueue = [(0, start)]
        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)
            # Skip if a shorter path has already been found
            if currentCost > distances[currentNode]:
                continue
            # If found the target node then return the cost
            if currentNode == end:
                return currentCost
            # Explore neighbors and update distances
            for edge in self.adjacencyList[currentNode]:
                neighbor, edgeLength = edge
                newRouteCost = edgeLength + distances[currentNode]
                # Update distance if a shorter route is found
                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue, (newRouteCost, neighbor))
        # Return the minimum distance or -1 if no path exists
        return -1 if distances[end] == float('inf') else distances[end]



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)


if __name__ == "__main__":
    test_cases = [
        ("Graph", [4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]]),
        ("shortestPath", [3, 2]),
        ("shortestPath", [0, 3]),
        ("addEdge", [[1, 3, 4]]),
        ("shortestPath", [0, 3])
    ]

    graph = None
    results = []

    for command, input in test_cases:
        if command == "Graph":
            n, edges = input
            graph = Graph(n, edges)
            results.append(None)
            print(termcolor.colored(f"Initialized Graph with {n} nodes and edges: {edges}", "yellow"))

        elif command == "addEdge":
            edge = input[0]
            graph.addEdge(edge)
            results.append(None)
            print(termcolor.colored(f"Added edge: {edge}", "yellow"))

        elif command == "shortestPath":
            node1, node2 = input
            cost = graph.shortestPath(node1, node2)
            results.append(cost)
            print(termcolor.colored(f"Shortest path cost from {node1} to {node2}: {cost}", "yellow"))

    print(termcolor.colored("\nFinal Results:", "green"))
    print(termcolor.colored(f"Test Cases: {test_cases}", "cyan"))
    print(termcolor.colored(f"Output: {results}", "green"))

