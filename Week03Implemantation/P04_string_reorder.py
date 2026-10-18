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
    string_reorder()

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def string_reorder():
    data = input("영어와 숫자가 포함된 문자열을 입력하시오: ")
    result = []
    value = 0

    # 문자를 하나씩 확인하며
    for x in data:
        # 알파벳인 경우 결과 리스트에 삽입
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)

    # 알파벳을 오름차순으로 정렬
    result.sort()

    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))

    # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
    print(f"재정렬된 문자열(영문자 정렬 & 숫자 합계) = {''.join(result)}")

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
