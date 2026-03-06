# BOJ 10816 - 숫자 카드 2
# URL: https://www.acmicpc.net/problem/10816
# Tier: Silver IV
# Tags: 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵

import sys
from typing import Counter
input = sys.stdin.readline

def solve() -> None:
    sg = int(input())
    sg_have=list(map(int,input().split()))
    you = int(input())
    you_have=list(map(int,input().split()))

    count_dict =Counter(sg_have)
    have=[]
    for i in you_have:
        have.append(count_dict[i])
    
    print(*have)


if __name__ == "__main__":
    solve()
