from datetime import datetime
from collections import deque
from turtle import resetscreen
from unittest import result


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))


    result = 0
    for i in range(n):
        for j in range(m):
            if dfs_icing(graph, n, m, i, j) == True:
                result += 1

    print(result)

def dfs_icing(graph, n, m, x, y):
    if x <= -1 or x>=n or y <= 1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs_icing(graph, n, m, x -1, y)
        dfs_icing(graph, n, m, x, y - 1)
        dfs_icing(graph, n, m, x + 1, y)
        dfs_icing(graph, n, m, x, y + 1)
        return True
    return False


def getCurrentTimeStr():
    return "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "]"

if __name__ == "__main__":


    startTime = datetime.now()
    print(getCurrentTimeStr(), "Starting the Greedy Algorithm Basic Program...")

    programStart()
    finishTime = datetime.now()
    executionTime = finishTime - startTime
    print(getCurrentTimeStr(), "Program execution completed.")
    print(getCurrentTimeStr(), f"Execution time: {executionTime}")
