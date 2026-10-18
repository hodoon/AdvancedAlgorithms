## 기본 라이브러리 임포트
from datetime import datetime
import os
## 추가 라이브러리
from collections import deque

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.

    n = int(input("숫자를 입력하시오: "))
    print(f"반복적으로 구현한 {n}!: {factorial_interative(n)}")
    print(f"재귀적으로 구현한 {n}!: {factorial_recursive(n)}")



    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def factorial_interative(n):
    result = 1

    if n == 0:
        return result

    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1: # n이 1이하인 경우 1을 반환
        return 1

    # n! = n * (n-1)!를 그대로 코드로 작성
    return n * factorial_recursive(n-1)

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
