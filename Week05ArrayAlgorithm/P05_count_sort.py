## 기본 라이브러리 임포트
from ast import While
from datetime import datetime

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    # array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"초기 데이터 배열: {array}")

    sorted_array, operation_cnt = count_sort(array.copy())


    print(f"정렬된 데이터 배열: {sorted_array}")
    print(f"정렬하는데 비교한 횟수: {operation_cnt}")

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def count_sort(array):
    operation_cnt = 0

    # 모든 원소의 값이 0보다 크거나 같다고 가정, 정렬을 위한 공간을 데이터=배열인덱스로, 단순하게 생성할 수 있음
    # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
    count_map = [0] * (max(array) + 1)
    sorted_array = []

    for i in range(len(array)):
        operation_cnt += 1
        count_map[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

    for i in range(len(count_map)): # 리스트에 기록된 정렬 정보 확인
        operation_cnt += 1
        for j in range(count_map[i]):
            sorted_array.append(i) # 등장한 횟수만큼 인덱스(데이터) 출력

    return sorted_array, operation_cnt

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
