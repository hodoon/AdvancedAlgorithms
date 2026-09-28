from datetime import datetime
from collections import deque
from pickletools import read_uint1
from posix import putenv
from queue import PriorityQueue
import re

def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed

    n = 5
    f_val = factorial_iterative(n)
    r_val = factorial_recursive(n)
    print(f"{n}! 은 {f_val}")
    print(f"재귀함수 {n}! 은 {r_val}")

def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result = result * i

    return result

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
