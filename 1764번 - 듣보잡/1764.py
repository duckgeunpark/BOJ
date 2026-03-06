# BOJ 1764 - 듣보잡
# URL: https://www.acmicpc.net/problem/1764
# Tier: Silver IV
# Tags: 자료 구조, 문자열, 정렬, 집합과 맵, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

def solve() -> None:
    a,b = map(int,input().split())
    unknown=[]
    see=set()
    hear=set()
    for _ in range(a):
        see.add(input().strip())
    for _ in range(b):
        hear.add(input().strip())

    for name in see :
        if name in hear :
            unknown.append(name)
    unknown.sort()
    print(len(unknown))
    for i in unknown :
        print(i)

if __name__ == "__main__":
    solve()
