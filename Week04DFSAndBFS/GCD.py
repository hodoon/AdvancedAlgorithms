from datetime import datetime
from collections import deque

def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed

    a, b= 192, 162
    print(f"{a}와 {b}의 최대공약수는 {gcd(a, b)}이다.")

def gcd(a,b):
    print(f"gcd({a}, {b})")
    if(a%b) == 0:
        return b
    return gcd(b, a % b)

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
