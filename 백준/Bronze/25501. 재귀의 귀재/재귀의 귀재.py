# BOJ 25501 - 재귀의 귀재
# URL: https://www.acmicpc.net/problem/25501
# Tier: Bronze II
# Tags: 구현, 문자열, 재귀

import sys
input = sys.stdin.readline
count = 0

def recursion(s:str, l:int, r:int) :    
    global count
    count += 1
    if(l >= r) :
        return 1
    elif(s[l] != s[r]) :
        return 0
    else :
        return recursion(s, l+1, r-1)

count = 0
def solve() -> None:
    global count
    num = int(input())
    for _ in range(num):
        count = 0
        rind= input().strip()
        result= recursion(rind,0,len(rind)-1)
        print(f'{result} {count}')

    

if __name__ == "__main__":
    solve()
