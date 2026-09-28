from datetime import datetime


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    stackExample()


def stackExample():

    stack = []
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    print(stack)

    popData = stack.pop()
    print(popData)
    print(stack)

    stack.append(1)
    stack.append(4)
    popData = stack.pop()
    print(popData)
    print(stack)

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
