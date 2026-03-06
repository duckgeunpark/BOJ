# BOJ 14425 - 문자열 집합
# URL: https://www.acmicpc.net/problem/14425
# Tier: Silver IV
# Tags: 자료 구조, 문자열, 집합과 맵, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

import sys
input = sys.stdin.readline

def solve() -> None:
    N , M = map(int,input().split())
    Ns = []
    Ms = []
    count= 0
    for i in range(N) :
        Ns.append(input().split())
    for i in range(M) :
        Ms.append(input().split())

    for word in Ms :
        if word in Ns :
            count += 1
            
    print(count)


if __name__ == "__main__":
    solve()
