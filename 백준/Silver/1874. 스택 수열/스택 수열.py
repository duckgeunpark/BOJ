# BOJ 1874 - 스택 수열
# URL: https://www.acmicpc.net/problem/1874
# Tier: Silver II
# Tags: 자료 구조, 스택

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    stack = []
    result = []
    num = 1

    for x in nums:
        while num <= x:
            stack.append(num)
            result.append("+")
            num += 1

        if stack[-1] == x:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            return

    print("\n".join(result))


if __name__ == "__main__":
    solve()

