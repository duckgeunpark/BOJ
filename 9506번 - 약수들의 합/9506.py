# BOJ 9506 - 약수들의 합
# URL: https://www.acmicpc.net/problem/9506
# Tier: Bronze I
# Tags: 수학, 구현, 정수론

import sys
input = sys.stdin.readline

def solve() -> None:
    while(1):
        num=int(input())
        nums=[]
        sum=0
        if num==-1:
            break
        
        for i in range(1,num):
            if num% i == 0:
                nums.append(i)
                sum+=i
        
        if sum==num :
            print(f"{num} = {' + '.join(map(str, nums))}")
        else :
            print(f'{num} is NOT perfect.')
  
if __name__ == "__main__":
    solve()
