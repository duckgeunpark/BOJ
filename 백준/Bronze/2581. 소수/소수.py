# BOJ 2581 - 소수
# URL: https://www.acmicpc.net/problem/2581
# Tier: Bronze II
# Tags: 소수 판정, 정수론, 수학

import sys
input = sys.stdin.readline

def solve() -> None:
    minn = int(input())
    maxx = int(input())
    nums=[]
    
    for i in range(minn,maxx+1):
        count = 0
        for j in range(1,i+1):
            if i % j==0:
                count += 1
        if count == 2:
            nums.append(i)
    if nums :
        print(sum(nums))
        print(min(nums))
    else :
        print("-1")
            

if __name__ == "__main__":
    solve()
