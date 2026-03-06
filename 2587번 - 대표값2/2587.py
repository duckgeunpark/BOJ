# BOJ 2587 - 대표값2
# URL: https://www.acmicpc.net/problem/2587
# Tier: Bronze II
# Tags: 수학, 구현, 정렬, 사칙연산

import sys
input = sys.stdin.readline

def solve() -> None:
    num = [int(input().strip()) for _ in range(5)]
    num.sort()
    avg = sum(num)//5

    print (avg)
    print (num[2])
if __name__ == "__main__":
    solve()
