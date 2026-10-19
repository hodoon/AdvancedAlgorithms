## 기본 라이브러리 임포트
from datetime import datetime
import os
from random import randint
from time import time

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.
    # array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"초기 데이터 배열: {array}")

    sorted_array = None
    operation_cnt = None

    sorted_array, operation_cnt = insertion_sort(array.copy())

    print(f"정렬된 데이터 배열: {sorted_array}")
    print(f"정렬하는데 비교한 횟수: {operation_cnt}")

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def insertion_sort(array):
    operation_cnt = 0
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복
            operation_cnt += 1
            if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
                array[j], array[j - 1] = array[j - 1], array[j]
            else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
    return array, operation_cnt


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
