# BOJ 25305 - 커트라인
# URL: https://www.acmicpc.net/problem/25305
# Tier: Bronze II
# Tags: 구현, 정렬

import sys
input = sys.stdin.readline

def solve() -> None:
    N, k = map(int, input().split())
    x = list(map(int, input().split()))

    # 점수가 높은 순서대로(내림차순) 정렬
    x.sort(reverse=True)
    
    # 상위 k번째 사람의 점수 (인덱스는 0부터 시작하므로 k-1)
    print(x[k-1])

if __name__ == "__main__":
    solve()