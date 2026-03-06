# BOJ 1181 - 단어 정렬
# URL: https://www.acmicpc.net/problem/1181
# Tier: Silver V
# Tags: 문자열, 정렬

import sys
input = sys.stdin.readline

def solve() -> None:
    N = int(input())
    word = [input().strip() for _ in range(N)]
    words = list(set(word))
    
    words.sort()
    words.sort(key=len)

    for word in words : 
        print(word)

if __name__ == "__main__":
    solve()
