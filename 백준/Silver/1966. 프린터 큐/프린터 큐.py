# BOJ 1966 - 프린터 큐
# URL: https://www.acmicpc.net/problem/1966
# Tier: Silver III
# Tags: 구현, 자료 구조, 시뮬레이션, 큐

from collections import deque
import sys

input = sys.stdin.readline


def printno(n: int, target: int, importantt: list) -> int:
    # (중요도, 초기 위치) 형태로 큐 초기화
    q = deque([(val, idx) for idx, val in enumerate(importantt)])
    turn = 0

    while q:
        current = q.popleft()  # 1. 큐의 가장 앞에 있는 문서를 꺼냄

        # 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 것이 있는지 확인
        if any(current[0] < doc[0] for doc in q):
            q.append(current)  # 중요도가 높은 게 있다면 맨 뒤로 보냄
        else:
            turn += 1  # 없다면 인쇄 (turn 증가)
            if current[1] == target:  # 인쇄한 문서가 우리가 찾는 대상이면 종료
                return turn


def solve() -> None:
    t = int(input())  # 테스트 케이스 개수
    for _ in range(t):
        n, m = map(int, input().split())  # m이 target(목표 인덱스)
        importantt = list(map(int, input().split()))
        ans = printno(n, m, importantt)
        print(ans)


if __name__ == "__main__":
    solve()
