# BOJ 1676 - 팩토리얼 0의 개수
# URL: https://www.acmicpc.net/problem/1676
# Tier: Silver V
# Tags: 수학

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    fect = 1
    while n:
        fect *= n
        n -= 1
    fect = str(fect)
    count = 0
    for i in range(len(fect) - 1, -1, -1):
        if fect[i] == "0":
            count += 1
        else:
            break
    print(count)


if __name__ == "__main__":
    solve()
