# BOJ 11653 - 소인수분해
# URL: https://www.acmicpc.net/problem/11653
# Tier: Bronze I
# Tags: 수학, 정수론, 소수 판정, 소인수분해

import sys
input = sys.stdin.readline

def solve() -> None:
    num=int(input())
    if num == 1:
        return
    i =2
    while num > 1:
        if num % i == 0:
            print(i)
            num=num//i
        else :
            i += 1


if __name__ == "__main__":
    solve()
