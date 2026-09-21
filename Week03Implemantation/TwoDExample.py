from datetime import datetime


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    twoDExample()

def twoDExample():
    for i in range(0, 5):
        for j in range(0, 5):
            print(f"({i}, {j})", end=" ")
        print()

        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

        x, y = 0, 2

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0) and (nx < 5) and (ny >= 0) and (ny < 5):
                print(f"The next possible locations: ({nx}, {ny})")


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