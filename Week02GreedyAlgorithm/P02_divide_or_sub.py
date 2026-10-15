## 기본 라이브러리 임포트
from datetime import datetime
import os
## 추가 라이브러리

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하시오.

    n, k = map(int, input("").split())

    divide_or_sub01(n, k)
    divide_or_sub02(n, k)
    divide_or_sub03(n, k)


    ###########################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def divide_or_sub01(n, k):

    result = 0
    steps = [(0, "", n)]
    logs = []

    while n >= k:
        while n % k != 0:
            previous_n = n
            n -= 1
            result += 1
            steps.append((len(steps), "N-1", n))
            logs.append(f"N={previous_n}, N % K={previous_n % k} → N=N-1={n}, result={result}")

        previous_n = n
        n //= k
        result += 1
        steps.append((len(steps), "N / K", n))
        logs.append(f"N={previous_n}, N % K=0 → N=N//K={n}, result={result}")

    while n > 1:
        previous_n = n
        n -= 1
        result += 1
        steps.append((len(steps), "N-1", n))
        logs.append(f"N={previous_n}, N<K → N=N-1={n}, result={result}")

    print("dos01 계산 로그 (1씩 빼며 나누어 떨어지는 수 찾기):")
    for log in logs:
        print(" ", log)
    printSteps(steps)
    print(f"dos01 결과값: {result}")

def divide_or_sub02(n, k):

    result = 0
    steps = [(0, "", n)]
    logs = []

    while n >= k:
        target = (n // k) * k
        subtract_count = n - target
        logs.append(f"target=({n}//{k})*{k}={target}; 감산 횟수={n}-{target}={subtract_count}")
        result += subtract_count
        for value in range(n - 1, target - 1, -1):
            steps.append((len(steps), "N-1", value))
        n = target

        previous_n = n
        n //= k
        result += 1
        steps.append((len(steps), "N / K", n))
        logs.append(f"N={previous_n} → N=N//K={n}; 나눗셈 1회, result={result}")

    while n > 1:
        previous_n = n
        n -= 1
        result += 1
        steps.append((len(steps), "N-1", n))
        logs.append(f"N={previous_n}, N<K → 남은 감산 1회, N={n}, result={result}")

    print("dos02 계산 로그 (목표값까지의 감산 횟수를 한 번에 계산):")
    for log in logs:
        print(" ", log)
    printSteps(steps)
    print(f"dos02 결과값: {result}")

def printSteps(steps):
    print("| 단계 | 연산 과정 | N의 값 |")
    print("| --- | --- | ---: |")
    for step, operation, value in steps:
        print(f"| {step}단계 | {operation} | {value} |")

## While문 최소 한번 더 줄이기
def divide_or_sub03(n, k):

    result = 0
    steps = [(0, "", n)]
    logs = []

    # N이 K보다 작은 경우, 최초부터 while 문을 실행하지 않음
    while n >= k:
        # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
        target = (n // k) * k
        subtract_count = n - target
        result += subtract_count
        logs.append(f"target=({n}//{k})*{k}={target}; result += {n}-{target}={subtract_count} → {result}")
        for value in range(n - 1, target - 1, -1):
            steps.append((len(steps), "N-1", value))

        n = target
        logs.append(f"N=target={n}")
        previous_n = n
        n = n // k
        result += 1
        steps.append((len(steps), "N / K", n))
        logs.append(f"N={previous_n} → N=N//K={n}; result += 1 → {result}")

    # 마지막으로 남은 수에 대하여 1씩 빼기
    while n > 1:
        previous_n = n
        n -= 1
        result += 1
        steps.append((len(steps), "N-1", n))
        logs.append(f"N={previous_n}, N<K → N=N-1={n}, result={result}")

    print("dos03 계산 로그 (감산 횟수를 더한 뒤 N을 target으로 갱신):")
    for log in logs:
        print(" ", log)
    printSteps(steps)
    print(f"dos03 결과값: {result}")


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
