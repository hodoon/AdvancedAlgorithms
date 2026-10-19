## 기본 라이브러리 임포트
from ast import While
from datetime import datetime
import os

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

    sorted_array, operation_cnt = quick_sort(array.copy())


    print(f"정렬된 데이터 배열: {sorted_array}")
    print(f"정렬하는데 비교한 횟수: {operation_cnt}")

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def quick_sort(array):
    operation_cnt = 0

    def quick_sort(array, start, end):
        operation_cnt = 0
        if start >= end: # 원소가 1개인 경우 종료
            return 0
        pivot = start # 피벗은 첫 번째 원소
        left = start + 1
        right = end
        while(left <= right):
            operation_cnt += 1

            # 피벗보다 큰 데이터를 찾을 때까지 반복
            while(left <= end and array[left] <= array[pivot]):
                operation_cnt += 1
                left += 1

            # 피벗보다 작은 데이터를 찾을 때까지 반복
            while(right > start and array[right] >= array[pivot]):
                operation_cnt += 1
                right -= 1

            if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
                array[right], array[pivot] = array[pivot], array[right]
            else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
                array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        operation_cnt += quick_sort(array, start, right-1)
        operation_cnt += quick_sort(array, right+1, end)

        return operation_cnt

    operation_cnt +=  quick_sort(array, 0, len(array) - 1)
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
