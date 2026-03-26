# BOJ 4153 - 직각삼각형
# URL: https://www.acmicpc.net/problem/4153
# Tier: Bronze III
# Tags: 수학, 기하학, 피타고라스 정리

import sys

input = sys.stdin.readline


def solve() -> None:
    while True:
        chektri = list(map(int, input().split()))
        chektri.sort()
        if 0 in chektri:
            break

        if chektri[0] ** 2 + chektri[1] ** 2 == chektri[2] ** 2:
            print("right")
        else:
            print("wrong")


if __name__ == "__main__":
    solve()
