# BOJ 1920 - 수 찾기
# URL: https://www.acmicpc.net/problem/1920
# Tier: Silver IV
# Tags: 자료 구조, 정렬, 이분 탐색, 집합과 맵, 해시를 사용한 집합과 맵


import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = tuple(map(int, input().split()))
    for i in B:
        print(1 if i in A else 0)


if __name__ == "__main__":
    solve()

