## 기본 라이브러리 임포트
from datetime import datetime
import os

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(f"초기 데이터 배열: {array}")

    sorted_array = None
    operation_cnt = None

    sorted_array, operation_cnt = selection_sort(array.copy())

    print(f"정렬된 데이터 배열: {sorted_array}")
    print(f"정렬하는데 비교한 횟수: {operation_cnt}")

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def selection_sort(array):
    operation_cnt = 0
    for i in range(len(array)):
        min_index = i # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            operation_cnt += 1
            if array[min_index] > array[j]:
                min_index = j
        # 스와프
        array[i], array[min_index] = array[min_index], array[i]
        # temp = array[i]
        # array[i] = array[min_index]
        # array[min_index] = temp
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
