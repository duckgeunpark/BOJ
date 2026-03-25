# BOJ 28278 - 스택 2
# URL: https://www.acmicpc.net/problem/28278
# Tier: Silver IV
# Tags: 자료 구조, 스택

import sys
import tabnanny

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    stack = []
    for _ in range(n):
        temp = []
        temp = list(map(int, input().split()))
        a = temp[0]
        b = temp[1] if len(temp) > 1 else 0
        if a == 1:
            stack.append(b)
        elif a == 2:
            if len(stack) > 0:
                print(stack.pop())
            else:
                print(-1)
        elif a == 3:
            print(len(stack))
        elif a == 4:
            if len(stack) > 0:
                print(0)
            else:
                print(1)
        elif a == 5:
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)


if __name__ == "__main__":
    solve()

