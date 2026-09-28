from datetime import datetime
from collections import deque


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    queueExample()


def queueExample():
    queue = deque()
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    popData = queue.popleft()
    print(popData)
    print(queue)
    queue.append(1)
    queue.append(4)
    print(queue)
    queue.popleft()
    print(queue)

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
