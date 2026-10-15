## 기본 라이브러리 임포트
from datetime import datetime
import os
## 추가 라이브러리

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.

    multiply_or_devide()

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")


#########################################################################################
#########################################################################################
#########################################################################################

def multiply_or_devide():
    data = input()

    # 첫 번째 문자를 숫자로 변경하여 대입
    result = int(data[0])

    for i in range(1, len(data)):
        # 두 수 중에서 하나라도 '0'혹은 '1'인 경우, 곱하기보다는 더하기 수행
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num

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
