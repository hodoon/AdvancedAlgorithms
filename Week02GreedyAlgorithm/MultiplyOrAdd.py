## 각 자리가 숫자 (0 부터 9)로 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하여라
## 단, +보다 x 연산자를 먼저 계산하는 일반적인 방식과 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정
## 예를 들어 02984라는 문자열이 주어지면, 만들어질 수 있는 가장 큰 수는 ((((0+2)x9)x8)x4) = 576이 된다.
## 또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력하여야 한다.
from datetime import datetime


def programStart():
    print("Welcome to the Adventurer Guild Program!")
    multiplyOrAdd()


def multiplyOrAdd():
    data = input("Enter a string of digits (0-9): ")
    result = int(data[0])

    for i in range(1, len(data)):
        num = int(data[i])
        if (num <= 1) or (result <= 1):
            result += num
        else:
            result *= num

    print(result)

    return result

def getCurrentTimeStr():
    from datetime import datetime
    return "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "]"


if __name__ == "__main__":

    startTime = datetime.now()
    print(getCurrentTimeStr(), "Starting the Adventurer Guild Program...")
    programStart()
    finishTime = datetime.now()
    excutionTime = finishTime - startTime  # Calculate the actual execution time
    print(getCurrentTimeStr(), "Program execution completed.", excutionTime)