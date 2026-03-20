# BOJ 4948 - 베르트랑 공준
# URL: https://www.acmicpc.net/problem/4948
# Tier: Silver II
# Tags: 수학, 정수론, 소수 판정, 에라토스테네스의 체

import sys
import math

input = sys.stdin.readline


def is_frime(n: int) -> list:
    is_frime = [True] * ((2 * n) + 1)
    is_frime[0] = is_frime[1] = False

    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if is_frime[i]:
            for j in range(i * i, ((2 * n) + 1), i):
                is_frime[j] = False
    return is_frime


def solve() -> None:
    while 1:
        num = int(input())
        if num == 0:
            break
        frime_list = is_frime(num)
        count = sum(1 for i in range(num + 1, 2 * num + 1) if frime_list[i])
        print(count)


if __name__ == "__main__":
    solve()
