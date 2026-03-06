# BOJ 11478 - 서로 다른 부분 문자열의 개수
# URL: https://www.acmicpc.net/problem/11478
# Tier: Silver III
# Tags: 자료 구조, 문자열, 집합과 맵, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

import sys
input = sys.stdin.readline

def solve() -> None:
    string=input().strip()
    result=set()
    
    for i in range(len(string)) :
        for j in range(i+1, len(string)+1):
            result.add(string[i:j])

    print(len(result))
    
   
if __name__ == "__main__":
    solve()
