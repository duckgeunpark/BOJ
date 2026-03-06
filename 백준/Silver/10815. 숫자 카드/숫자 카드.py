# BOJ 10815 - 숫자 카드
# URL: https://www.acmicpc.net/problem/10815
# Tier: Silver V
# Tags: 자료 구조, 정렬, 이분 탐색, 집합과 맵, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

def solve() -> None:
    sg = int(input())
    sg_have = set(map(int,input().split()))
    you = int(input())
    you_have = list(map(int,input().split()))
    answer= []
    for num in you_have :
        if num in sg_have:
            answer.append(1)
        else :
            answer.append(0)
    
    print(*answer)

if __name__ == "__main__":
    solve()
