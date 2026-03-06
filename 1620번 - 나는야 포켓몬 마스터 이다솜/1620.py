# BOJ 1620 - 나는야 포켓몬 마스터 이다솜
# URL: https://www.acmicpc.net/problem/1620
# Tier: Silver IV
# Tags: 자료 구조, 집합과 맵, 해시를 사용한 집합과 맵

import numbers
import sys
input = sys.stdin.readline

def solve() -> None:
    dic,what = map(int,input().split())
    num_to_name = {}
    name_to_num = {}
    for i in range(1,dic+1):
        name = input().strip()
        num_to_name[i]=name
        name_to_num[name]=i

    for _ in range(what) :
        query = input().strip()

        if query.isdigit():
            print(num_to_name[int(query)])
        else :
            print(name_to_num[query])
        
if __name__ == "__main__":
    solve()
