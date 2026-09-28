from datetime import datetime
from collections import deque


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed

    i = 1
    recursiveFunction_withFinish(i)


def recursiveFunction_withFinish(i):
    if i == 5:
        print(f"{i}번째 함수를 종료합니다.")
        return

    print(f"{i}번째 함수에서, {i+1}번째 함수를 호출합니다.]")
    recursiveFunction_withFinish(i+1)
    print(f"{i}번째 함수를 종료합니다.")



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
