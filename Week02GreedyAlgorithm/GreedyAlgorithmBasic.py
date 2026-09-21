from datetime import datetime

def programStart():
    getChangeCnt()

def getChangeCnt():
    n = 1260
    count = 0

    array = [500, 100, 50, 10]

    for coin in array:
        count += (n // coin)
        n %= coin

    print("거슬러 주어야 할 동전의 최소 개수:", count)

def getCurrentTimeStr():
    return "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "]"


if __name__ == "__main__":

    startTime = datetime.now()
    print(getCurrentTimeStr(), "Starting the Greedy Algorithm Basic Program...")
    programStart()
    endTime = datetime.now()
    executionTime = endTime - startTime
    print(getCurrentTimeStr(), "Program execution completed. Total Execution Time:", executionTime)