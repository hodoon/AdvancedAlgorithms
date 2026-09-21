from datetime import datetime


def programStart():
    print("Welcome to the Greedy Algorithm Basic Program!")
    # Add more functionality here as needed
    upDownLeftRight()

def upDownLeftRight():
    n = int(input("Enter a number: "))
    x, y = 1, 1
    plans = input().split()

    # L, R, U, D에 따른 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types =['L', 'R', 'U', 'D']

    # 이동 계획을 하나씩 확인하기
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            # if plan == move_types[i]:
            #     nx = x + dx[i]
            #     ny = y + dy[i]
            i = move_types.index(plan)
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or nx > n or ny < 1 or ny > n:
            print("Invalid move!")
            continue
        x = nx
        y = ny

    print("Final Location: ", x, y)
    print(f"Final Location: {x}, {y}")

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