# BOJ 2630 - 색종이 만들기
# URL: https://www.acmicpc.net/problem/2630
# Tier: Silver II
# Tags: 분할 정복, 재귀

import sys

input = sys.stdin.readline

blue = 0
white = 0
paper = []


def cutpaper(x: int, y: int, n: int) -> None:
    global blue, white
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                half = n // 2
                cutpaper(x, y, half)
                cutpaper(x, y + half, half)
                cutpaper(x + half, y, half)
                cutpaper(x + half, y + half, half)
                return
    if color == 1:
        blue += 1
    else:
        white += 1


def solve() -> None:
    global paper
    n = int(input())

    for _ in range(n):
        paper.append(list(map(int, input().split())))

    cutpaper(0, 0, n)
    print(white)
    print(blue)


if __name__ == "__main__":
    solve()
