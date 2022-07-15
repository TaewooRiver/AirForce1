import sys
f = sys.stdin.readline
from collections import deque

n, l, r = map(int, f().split())
graph = []

# union = [[-1] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, f().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def process(x, y, index):
    # nationsUnited는 나중에 연합끼리 인구수 평균으로 맞추기 위해 사용
    nationsUnited = []
    nationsUnited.append((x, y))
    # 옆 칸과 연합 가능여부를 알기 위해 DFS
    q = deque()
    q.append((x, y))
    # union지도에 인덱스 표시
    # 인덱스의 종류는 0부터 (n*n - 1)까지 있을 수 있으나 다 쓰이지는 않음
    union[x][y] = index
    # 나중에 summary // count 로 평균 인구수 구할것임.
    # 각 연합마다 summary와 count값을 초기화해야하므로 다음과 같이 설정
    summary = graph[x][y]
    count = 1
    # n * n 리스트에서 BFS 수행
    while q:
        # 큐에서 하나 뽑아서
        x, y = q.popleft()
        # 네 방향으로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고 연합이 아직 없을경우
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 본 칸이랑 인구수 차이가 허용범위이면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    # 큐에다 삽입
                    q.append((nx, ny))
                    # 연합 번호 부여
                    union[nx][ny] = index
                    # 있다가 평균값 구하기 위해 summary, count에 더해줌
                    summary += graph[nx][ny]
                    count += 1
                    # 구해진 평균값을 배분하기 위해 nationsUnited에 위치 저장
                    nationsUnited.append((nx, ny))
    for i, j in nationsUnited:
        graph[i][j] = summary // count
    
# 인구이동 이루어진 횟수
total_count = 0

# 더 이상 연합을 할 수 없을 때까지
while True:
    # 매 연합마다 다시 국경을 닫아야하므로 다음과 같이 union, index를 초기화
    union = [[-1]*n for _ in range(n)]
    index = 0
    # 각 칸에 대해
    for i in range(n):
        for j in range(n):
            # 연합 가입 안 됐으면
            if union[i][j] == -1:
                # 연합을 새로 만들어서 BFS로 퍼져 나가기
                process(i, j, index)
                index += 1
    # 만약 더 이상 인구 이동이 일어나지 않으면 
    # "index += 1"이 총 n*n번 실행되었을 것이므로
    # 매번 0으로 초기화되는 index가 n * n이 된다는 것은 더 이상 인구이동이 없다는 뜻.
    # 이는 total_count에 1을 더할 수 있는 유효한 회차가 아니므로 여기서 break
    if index == n * n:
        break
    total_count += 1

print(total_count)