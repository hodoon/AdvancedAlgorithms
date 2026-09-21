## 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정을 만듦
## 동빈이가 최대 몇개의 모험가 그룹을 만들 수 있는가? N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 구룹 수의 최댓값을 구하는 프로그램을 작성하라

## 예를 들어 N=5이고, 각 모험가의 공포도가 다음과 같다고 가정하면, [2 3 1 2 2]
## 이 경우 그룹 1에 공포도가 1, 2, 3인 모험가를 한 명씩 넣고 그룹 2에 공포도가 2인 남은 두 명을 넣게 되면 총 2개의 그룹을 만들 수 있다. 
## 따라서 이 경우에 대한 정답은 2가 된다.
from datetime import datetime


def programStart():
    print("Welcome to the Adventurer Guild Program!")
    adventurerGuild()

def adventurerGuild():
    n = int(input("Enter the number of adventurers: "))
    data = list(map(int, input("Enter the fear levels of the adventurers separated by space: ").split()))
    data.sort()  # Sort the fear levels in ascending order

    result = 0  # The number of groups formed
    count = 0  # The number of adventurers in the current group

    for i in data:
        count += 1 # Include this adventurer in the current group
        if count >= i:
            result += 1  # Form a group
            count = 0  # Reset the count for the next group

    print(result)  # Print the number of groups formed

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