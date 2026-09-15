from datetime import datetime


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    kingdomsKnight()

def kingdomsKnight():
    input_data = input("Please enter your move: ")
    row = int(input_data[1])

    column = int(ord(input_data[0])) - int(ord('a')) + 1

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if next_row >= 1 or next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1

    result

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