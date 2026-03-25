# BOJ 11050 - 이항 계수 1
# URL: https://www.acmicpc.net/problem/11050
# Tier: Bronze I
# Tags: 수학, 구현, 조합론

import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(math.comb(m, n))
