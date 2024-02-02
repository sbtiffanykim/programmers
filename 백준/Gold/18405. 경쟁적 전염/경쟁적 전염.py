from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue):
    while queue:
        virus_type, time, x, y = queue.popleft()
        if time == s:  # 시간이 다 되면 바이러스 퍼뜨리기 멈추기
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] != 0:  # 이미 다른 바이러스가 있는 경우
                continue
            board[nx][ny] = virus_type
            queue.append((virus_type, time + 1, nx, ny))


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
queue = list()

for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            queue.append((board[i][j], 0, i, j))
queue.sort()
queue = deque(queue)
bfs(queue)  # 바이러스

print(board[x - 1][y - 1])