# BOJ 27433 - 팩토리얼 2
# URL: https://www.acmicpc.net/problem/27433
# Tier: Bronze V
# Tags: 수학, 사칙연산

import sys
input = sys.stdin.readline

def solve() -> None:
    n = int(input())
    fect(1,n)
def fect(mil,int) :
    if (int > 0) :
        mil *= int
        int -= 1
        fect(mil,int)
    else :
        print(mil)

if __name__ == "__main__":
    solve()