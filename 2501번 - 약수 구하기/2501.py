# BOJ 2501 - 약수 구하기
# URL: https://www.acmicpc.net/problem/2501
# Tier: Bronze III
# Tags: 수학, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

def solve() -> None:
    a,b = map(int,input().split())
    nums=[]
    count= 0
    for i in range(1, a + 1):
        if a % i == 0:
            nums.append(i)

    if len(nums) >= b:      
        print(nums[b - 1])   
    else:                   
        print(0) 



if __name__ == "__main__":
    solve()
