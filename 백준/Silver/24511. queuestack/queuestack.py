from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

q = deque()
for i in range(n):
    if a[i] == 0:      # 큐인 것만 순서대로 모음
        q.append(b[i])

ans = []
for x in c:
    q.appendleft(x)    # 새값 왼쪽 추가
    ans.append(q.pop())  # 오른쪽에서 출력!

print(*ans)