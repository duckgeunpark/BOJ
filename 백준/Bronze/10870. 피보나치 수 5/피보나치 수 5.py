# BOJ 10870 - 피보나치 수 5
# URL: https://www.acmicpc.net/problem/10870
# Tier: Bronze II
# Tags: 수학, 구현

import re
import sys
input = sys.stdin.readline

def fibo (n:int) -> int :
    if n <= 1 :
        return n
    
    return fibo(n - 1) + fibo(n - 2)


def solve() -> None:
    number = int(input())
    enswer=fibo(number)
    print(enswer)
    

    

if __name__ == "__main__":
    solve()
