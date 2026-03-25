# BOJ 10773 - 제로
# URL: https://www.acmicpc.net/problem/10773
# Tier: Silver IV
# Tags: 구현, 자료 구조, 스택

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    real = []
    tem = []
    for _ in range(n):
        tem.append(int(input()))
        if tem[-1] == 0:
            tem = []
            real.pop()
        else:
            real.append(tem[-1])

    print(sum(real))


if __name__ == "__main__":
    solve()
