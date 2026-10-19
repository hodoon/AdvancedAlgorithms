## 기본 라이브러리 임포트
from datetime import datetime
import os
## 추가 라이브러리
from random import randint
import time

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.

    # array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    # # array = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
    # # array = [9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ,1 ,0]
    # print(f"초기 데이터 배열: {array}")

    # sortedArray = None
    # operationCnt = None

    # # sortedArray, operationCnt = selectionSort(array.copy())
    # # sortedArray, operationCnt = insertionSort(array.copy())

    # # sortedArray, operationCnt = quickSort(array.copy())
    # # sortedArray, operationCnt = quickSort_py(array.copy())

    # # array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    # # sortedArray, operationCnt = countSort(array.copy())

    # print(f"정렬된 데이터 배열: {sortedArray}")
    # print(f"정렬하는데 비교한 횟수: {operationCnt}")


    # sortTimeCompare()

    # listItemSwap()


    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################
def listItemSwap():
    n, k = map(int, input("데이터의 갯수와 바꿔치기 가능 횟수를 입력하세요: ").split()) # N과 K를 입력 받기
    a = list(map(int, input("배열 A의 모든 원소를 입력하세요: ").split())) # 배열 A의 모든 원소를 입력 받기
    b = list(map(int, input("배열 B의 모든 원소를 입력하세요: ").split())) # 배열 B의 모든 원소를 입력 받기

    a.sort() # 배열 A는 오름차순 정렬 수행
    b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

    # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
    for i in range(k):
        # A의 원소가 B의 원소보다 작은 경우
        if a[i] < b[i]:
            # 두 원소를 교체
            a[i], b[i] = b[i], a[i]
        else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
            break

    print(f"배열 A의 모든 원소의 합의 최대값: {sum(a)}") # 배열 A의 모든 원소의 합을 출력



def sortTimeCompare():
    # 배열에 10,000개의 정수를 삽입
    array = []
    for _ in range(10000):
        # 1부터 100 사이의 랜덤한 정수
        array.append(randint(1, 100))

    ## 선택 정렬
    start_time = time.time()
    selectionSort(array.copy())
    end_time = time.time()
    print("선택 정렬 성능 측정:", end_time - start_time)

    ## 파이선 내장 정렬
    start_time = time.time()
    array.sort()
    end_time = time.time()
    print("리스트 내 기본 정렬 성능 측정:", end_time - start_time)

def countSort(array):
    operationCnt = 0

    # 모든 원소의 값이 0보다 크거나 같다고 가정, 정렬을 위한 공간을 데이터=배열인덱스로, 단순하게 생성할 수 있음
    # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
    countMap = [0] * (max(array) + 1)
    sortedArray = []

    for i in range(len(array)):
        operationCnt += 1
        countMap[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

    for i in range(len(countMap)): # 리스트에 기록된 정렬 정보 확인
        operationCnt += 1
        for j in range(countMap[i]):
            sortedArray.append(i) # 등장한 횟수만큼 인덱스(데이터) 출력

    return sortedArray, operationCnt


def quickSort_py(array):
    def quick_sort(array):
        # 리스트가 하나 이하의 원소만을 담고 있다면 종료
        if len(array) <= 1:
            return array
        pivot = array[0] # 피벗은 첫 번째 원소
        tail = array[1:] # 피벗을 제외한 리스트

        ## 전체 원소를 탐색 (시간 복잡도 증가), 별도의 리스트 생성 (기존 리스트의 원소 재배치가 아님. 공간복잡도 증가)
        left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분, pivot 보다 작은 원소들
        right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분, pivot 보다 큰 원소들

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

    return quick_sort(array), None


def quickSort(array):
    operationCnt = 0

    def quick_sort(array, start, end):
        operationCnt = 0
        if start >= end: # 원소가 1개인 경우 종료
            return 0
        pivot = start # 피벗은 첫 번째 원소
        left = start + 1
        right = end
        while(left <= right):
            operationCnt += 1

            # 피벗보다 큰 데이터를 찾을 때까지 반복
            while(left <= end and array[left] <= array[pivot]):
                operationCnt += 1
                left += 1

            # 피벗보다 작은 데이터를 찾을 때까지 반복
            while(right > start and array[right] >= array[pivot]):
                operationCnt += 1
                right -= 1

            if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
                array[right], array[pivot] = array[pivot], array[right]
            else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
                array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        operationCnt += quick_sort(array, start, right - 1)
        operationCnt += quick_sort(array, right + 1, end)

        return operationCnt

    operationCnt += quick_sort(array, 0, len(array) - 1)
    return array, operationCnt

def insertionSort(array):
    operationCnt = 0
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
            operationCnt += 1
            if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
                array[j], array[j - 1] = array[j - 1], array[j]
            else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break

    return array, operationCnt



def selectionSort(array):
    operationCnt = 0
    for i in range(len(array)):
        min_index = i # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            operationCnt += 1
            if array[min_index] > array[j]:
                min_index = j
        # 스와프
        array[i], array[min_index] = array[min_index], array[i]
        # temp = array[i]
        # array[i] = array[min_index]
        # array[min_index] = temp

    return array, operationCnt



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
