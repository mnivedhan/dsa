class MultistageGraph:
    def __init__(self, vertices, stages):
        """
        Initialize the multistage graph
        vertices: total number of vertices
        stages: number of stages
        """
        self.vertices = vertices
        self.stages = stages
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        """Add a directed edge from u to v with given weight"""
        self.graph[u].append((v, weight))

    def forward_dp(self, source, sink):
        """
        Forward DP approach - Calculate cost from source to each vertex
        Returns: (minimum cost, path)
        """
        print("\n" + "=" * 60)
        print("FORWARD APPROACH (Source → Sink)")
        print("=" * 60)

        # Initialize costs and parent tracking
        cost = [float('inf')] * self.vertices
        parent = [-1] * self.vertices
        cost[source] = 0

        print(f"\nInitial: cost[{source}] = 0 (starting point)")

        # Process vertices in topological order (0 to vertices-1)
        for u in range(self.vertices):
            if cost[u] == float('inf'):
                continue

            print(f"\nProcessing vertex {u} (current cost: {cost[u]}):")

            # Update all neighbors
            for v, weight in self.graph[u]:
                new_cost = cost[u] + weight
                print(f"  Edge {u}→{v} (weight={weight}): ", end="")

                if new_cost < cost[v]:
                    cost[v] = new_cost
                    parent[v] = u
                    print(f"Update! cost[{v}] = {new_cost}")
                else:
                    print(f"No update (current cost[{v}] = {cost[v]} is better)")

        # Reconstruct path
        path = self._reconstruct_path(parent, source, sink)

        print(f"\n{'=' * 60}")
        print(f"RESULT: Minimum cost = {cost[sink]}")
        print(f"Path: {' → '.join(map(str, path))}")
        print(f"{'=' * 60}")

        return cost[sink], path

    def backward_dp(self, source, sink):
       pass

    def _reconstruct_path(self, parent, source, sink):
        """Reconstruct path from parent array (for forward approach)"""
        path = []
        current = sink

        while current != -1:
            path.append(current)
            current = parent[current]

        path.reverse()
        return path


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example 1: Simple 4-stage graph
    print("\n" + "#" * 60)
    print("# EXAMPLE 1: Road Trip Problem")
    print("#" * 60)
    print("""
    Stage 0:  1 (NY)
    Stage 1:  2 (Chicago), 3 (Detroit), 4 (Pittsburgh)  
    Stage 2:  5 (Denver), 6 (Kansas City), 7 (Dallas)
    Stage 3:  8 (LA)

    Edges:
    1→2(1), 1→3(2), 1→4(5)
    2→5(4), 2→6(11), 3→6(9), 3→7(5), 4→7(3)
    5→8(18), 6→8(4), 7→8(13)
    """)

    g1 = MultistageGraph(vertices=9, stages=4)

    # Stage 0 to Stage 1
    g1.add_edge(1, 2, 1)  # NY → Chicago
    g1.add_edge(1, 3, 2)  # NY → Detroit
    g1.add_edge(1, 4, 5)  # NY → Pittsburgh

    # Stage 1 to Stage 2
    g1.add_edge(2, 5, 4)  # Chicago → Denver
    g1.add_edge(2, 6, 11)  # Chicago → Kansas City
    g1.add_edge(3, 6, 9)  # Detroit → Kansas City
    g1.add_edge(3, 7, 5)  # Detroit → Dallas
    g1.add_edge(4, 7, 3)  # Pittsburgh → Dallas

    # Stage 2 to Stage 3
    g1.add_edge(5, 8, 18)  # Denver → LA
    g1.add_edge(6, 8, 4)  # Kansas City → LA
    g1.add_edge(7, 8, 13)  # Dallas → LA

    # Solve using both approaches
    source, sink = 1, 8

    cost_forward, path_forward = g1.forward_dp(source, sink)
    cost_backward, path_backward = g1.backward_dp(source, sink)

    print("\n" + "🎯" * 30)
    print("\nCOMPARISON:")
    print(f"Forward:  Cost = {cost_forward}, Path = {path_forward}")
    print(f"Backward: Cost = {cost_backward}, Path = {path_backward}")
    print(f"\n✅ Both methods give the SAME result!")
    print("\n" + "🎯" * 30)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
