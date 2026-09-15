from datetime import datetime

def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    devidedCount = deviedFunc()
    print("Devied Count:", devidedCount)

def deviedFunc():
    n, k = map(int, input("Enter two integers n and k separated by space: ").split())

    count = 0

    while n >= k:
        # while n % k != 0:
        #     n -= 1
        #     count += 1
        target = (n // k) * k
        count += (n - target)

        n //= k
        count += 1

    # while n > 1:
    #     n -= 1
    #     count += 1
    count += (n - 1)

    return count

def getCurrentTimeStr():
    return "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "]"


if __name__ == "__main__":

    startTime = datetime.now()
    print(getCurrentTimeStr(), "Starting the Greedy Algorithm Basic Program...")
    programStart()
    endTime = datetime.now()
    executionTime = endTime - startTime
    print(getCurrentTimeStr(), "Program execution completed. Total Execution Time:", executionTime)