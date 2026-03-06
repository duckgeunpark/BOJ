# BOJ 1269 - 대칭 차집합
# URL: https://www.acmicpc.net/problem/1269
# Tier: Silver IV
# Tags: 자료 구조, 집합과 맵, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

import sys
input = sys.stdin.readline

def solve() -> None:
    a,b = map(int,input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    As=A-B
    Bs=B-A

    print(len(As)+len(Bs))

if __name__ == "__main__":
    solve()
