# BOJ 2720 - 세탁소 사장 동혁
# URL: https://www.acmicpc.net/problem/2720
# Tier: Bronze III
# Tags: 수학, 그리디 알고리즘, 사칙연산

import sys
input = sys.stdin.readline

def solve() -> None:
    N = int(input())
    coins = [25, 10, 5, 1]

    for _ in range(N):
        C = int(input())
        res = []
        for coin in coins:
            res.append(C // coin)
            C %= coin
        print(*res)

if __name__ == "__main__":
    solve()
