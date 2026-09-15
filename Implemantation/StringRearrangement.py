from datetime import datetime


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    StringRearrangement()

def StringRearrangement():
    print("StringRearrangement Starting...")
    data = input("Enter a string consisting only of uppercase English letters and numbers: ")
    result = []
    value = 0

    isIncludeNumber = False

    for x in data:
        if x.isalpha():
            result.append(x)
            print(result)
        elif x.isdigit():
            isIncludeNumber = True
            value += int(x)
        else:
            print(f"Invalid input. Please enter only uppercase English letters and numbers.{x}")

    result.sort()

    if isIncludeNumber:
        result.append(str(value))

    print(''.join(result))

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