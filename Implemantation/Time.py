from datetime import datetime


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    time()

def time():
    h = int(input())

    checkNum = "3"

    count = 0
    for i in range(h + 1):
        str_i = str(i)
        for j in range(60):
            str_j = str(j)
            for k in range(60):
                str_k = str(k)
                if checkNum in str_i + str_j + str_k:
                    count += 1

    print(count)

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