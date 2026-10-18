## 기본 라이브러리 임포트
from datetime import datetime
import os
from collections import deque

## 실행 함수
def programStart():
    print(getCurrentTimeStr(), "programStart() is started...")
    ############################################################
    ## 여기에 코드를 작성하세요.
    maze()
    ############################################################
    print(getCurrentTimeStr(), "programStart() is finished...")

#########################################################################################
#########################################################################################
#########################################################################################

def bfs_maze(graph, dx, dy, n, m, x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

def maze():
    n, m = map(int, input("미로의 세로, 가로 크기를 입력하시오: ").split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input(f"미로 인접행렬의 {i+1}번째 행 값을 입력하시오: "))))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(f"탈출읠 위해 움직여야 하는 최소 칸의 수: {bfs_maze(graph, dx, dy, n, m, 0, 0)}")
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
