## 기본 라이브러리 임포트
from ast import While
from datetime import datetime
import os
from turtle import right

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    # array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"초기 데이터 배열: {array}")

    sorted_array = None
    operation_cnt = None

    sorted_array, operation_cnt = quick_sort_py(array.copy())


    print(f"정렬된 데이터 배열: {sorted_array}")
    print(f"정렬하는데 비교한 횟수: {operation_cnt}")

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def quick_sort_py(array):
    def quick_sort(array):
        # 리스트 하나 이하의 원소만을 담고 있다면 종료
        if len(array) <= 1:
            return array
        pivot = array[0] # 피벗은 첫 번째 원소
        tail = array[1:] # 피벗을 제외한 리스트

        # 전체 원소를 탐색 (시간 복잡도 증가), 별도의 리스트 생성 (기존 리스트의 재배치가 아님. 공간복잡도 증가)
        left_side = [x for x in tail if x <= pivot] # 분할 왼쪽 부분, pivot보다 작은 원소들
        right_side = [x for x in tail if x > pivot] # 분할 오른쪽 부분, pivot보다 큰 원소들

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    return quick_sort(array), None

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
