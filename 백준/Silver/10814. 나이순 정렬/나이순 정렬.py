# BOJ 10814 - 나이순 정렬
# URL: https://www.acmicpc.net/problem/10814
# Tier: Silver V
# Tags: 정렬, 집합과 맵

import sys
input = sys.stdin.readline

def solve() -> None:
    num = int(input())
    members = []

    for _ in range(num):
        age, name = input().split()
        members.append([int(age), name])

    members.sort(key=lambda x: x[0])

    for age, name in members:
        print(f"{age} {name}")


if __name__ == "__main__":
    solve()
