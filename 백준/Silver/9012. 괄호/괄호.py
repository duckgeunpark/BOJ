# BOJ 9012 - 괄호
# URL: https://www.acmicpc.net/problem/9012
# Tier: Silver IV
# Tags: 자료 구조, 문자열, 스택

import sys

input = sys.stdin.readline


def checkps(s: str) -> str:
    cnt = 0
    for ch in s:
        if ch == "(":
            cnt += 1
        else:  # ch == ')'
            cnt -= 1
            # 닫는 괄호가 더 많아지면 바로 NO
            if cnt < 0:
                return "NO"
    # 전부 돌고 난 뒤에 0이면 YES, 아니면 NO
    return "YES" if cnt == 0 else "NO"


def solve() -> None:
    n = int(input())
    for _ in range(n):
        line = input().strip()
        print(checkps(line))


if __name__ == "__main__":
    solve()

