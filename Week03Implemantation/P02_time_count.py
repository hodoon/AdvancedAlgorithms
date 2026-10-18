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
    time_count()

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def time_count():
    # H를 입력받기
    h = int(input("시(hout)를 입력하시오: "))

    # 시각 문자에 포함돼 있는지 체크할 숫자
    check_num = 3

    count = 0

    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                if str(check_num) in str(i) + str(j) + str(k):
                    count += 1

    print(f"{check_num}이 포함된 시각의 총 수 = {count}")
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
