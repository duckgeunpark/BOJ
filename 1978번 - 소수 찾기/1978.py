# BOJ 1978 - 소수 찾기
# URL: https://www.acmicpc.net/problem/1978
# Tier: Bronze II
# Tags: 소수 판정, 정수론, 수학

import sys
input = sys.stdin.readline

def solve() -> None:
    n=int(input())
    nums=list(map(int,input().split()))
    sol = 0
    
    for i in range(n):
        count= 0
        for j in range(1,nums[i]+1):
            if nums[i]%j==0 :
                count += 1
        if count == 2 :
            sol +=1

    print (sol)
            

if __name__ == "__main__":
    solve()
