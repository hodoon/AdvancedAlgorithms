## 기본 라이브러리 임포트
from datetime import datetime
import os
from collections import deque

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.
    icing()

    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def dfs_icing(graph, n, m, x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs_icing(graph, n, m, x-1, y)
        dfs_icing(graph, n, m, x, y-1)
        dfs_icing(graph, n, m, x+1, y)
        dfs_icing(graph, n, m, x, y+1)
        return True
    return False

def icing():
    # N, M을 공백을 기준으로 구분하여 입력 받기
    n, m = map(int, input("세로 길이 N과 가로 길이 M을 입력하시오: ").split())

    # 2차원 리스트의 맵 정보 입력 받기
    graph = []
    for i in range(n):
        graph.append(list(map(int, input(f"세로 {i+1}번째 행의 가로 입력: "))))

    # 모든 노드(위치)에 대하여 음료수 채우기
    result = 0
    for i in range(n):
        for j in range(m):
            # 현재 윛치에서 DFS 수행
            if dfs_icing(graph, n, m, i, j) == True:
                result += 1

    print(f"얼음 조각은 총 {result}개 입니다.")

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
