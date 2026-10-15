## 기본 라이브러리 임포트
from datetime import datetime
import os
## 추가 라이브러리

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.

    adventure_guild()

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")


#########################################################################################
#########################################################################################
#########################################################################################

def adventure_guild():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    result = 0 # 총 그룹의 수
    count = 0 # 현재 그룹에 포함된 모험가의 수

    for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
        count += 1
        if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
            result += 1 # 총 그룹의 수 증가 시키기
            count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

    print(result)

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
