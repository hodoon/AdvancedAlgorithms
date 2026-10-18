## 기본 라이브러리 임포트
from datetime import datetime
import os
from traceback import print_tb
## 추가 라이브러리

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.

    move_LRUD()

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################
def move_LRUD():
    # N 입력받기
    n = int(input("공간의 가로/새로 크기를 입력하시오: "))
    x, y = 1, 1
    plans = input("이동 계획(L, R, U, D)을 순서대로 입력하시요: ").split()

    # L, R, U, D에 따른 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    # 이동 계획을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                # 공간을 벗어나는 경우 무시
                if nx < 1 or ny < 1 or nx > n or ny > n:
                    print(f"맵을 벗어남{nx}, {ny}")
                    continue
                # 이동 수행
                x, y = nx, ny
                print(f"현재 위치: ({x}, {y})")
    print(f"최종 도착 위치: ({x}, {y})")

#########################################################################################
#########################################################################################
#########################################################################################
##############################################################################
## 시간 출력을 위한 함수
def getCurrentTimeStr():
    currentTimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    return f"[{currentTimeStr}]"

##############################################################################
## 파이선 메인 함수, 파일을 실행시키면 여기부터 실행, 이 부분은 반드시 파일의 맨 마지막에 위치해야 함
if __name__ == "__main__":
    start_time = datetime.now()
    print(getCurrentTimeStr(), "main Start..")

    ##############
    ## 파이선의 메인 함수를 이용해서 실행할 함수
    programStart()
    ##############

    finish_time = datetime.now()
    print(getCurrentTimeStr(), f"main Finish..({(finish_time - start_time).total_seconds()}s Elapsed)")
