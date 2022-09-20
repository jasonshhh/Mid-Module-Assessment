# This code is from https://www.geeksforgeeks.org/floyd-warshall
# -algorithm-dp-16/
import sys

NO_PATH = sys.maxsize

graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
V = len(graph)


def floyd_warshall(dist):
    """
    dist[][] will be the output
    intermediate vertices
    """

    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):

                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )

    return dist


if __name__ == "__main__":
    floyd_warshall(graph)
