# BOJ 7785 - 회사에 있는 사람
# URL: https://www.acmicpc.net/problem/7785
# Tier: Silver V
# Tags: 자료 구조, 집합과 맵, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

def solve() -> None:
    num = int(input())
    names = set()
    for i in range(num):
        name,state =input().split()
        if state=="enter" :
            names.add(name)
        elif  state=="leave" :
            names.remove(name)
    sorted_names = sorted(names,reverse=True)
    for name in sorted_names :
        print(name)

if __name__ == "__main__":
    solve()
