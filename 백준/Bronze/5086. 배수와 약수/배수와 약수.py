# BOJ 5086 - 배수와 약수
# URL: https://www.acmicpc.net/problem/5086
# Tier: Bronze III
# Tags: 수학, 사칙연산

import sys
input = sys.stdin.readline

def solve() -> None:
    while(1):
        num =list(map(int,(input().split())))

        if num[0]==0 and num[1]==0:
            break
        
        if(num[1]%num[0]==0):
            print("factor")
        elif(num[0]%num[1]==0):
            print("multiple")
        else :
            print("neither")


if __name__ == "__main__":
    solve()
