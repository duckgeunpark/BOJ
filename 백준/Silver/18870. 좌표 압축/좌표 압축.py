# BOJ 18870 - 좌표 압축
# URL: https://www.acmicpc.net/problem/18870
# Tier: Silver II
# Tags: 정렬, 값 / 좌표 압축

import sys
input = sys.stdin.readline

def solve() -> None:
    N = int(input())
    X = list(map(int, input().split()))
    sorted_unique = sorted(list(set(X)))

    rank_dict = {value: index for index, value in enumerate(sorted_unique)}
    new = [str(rank_dict[num]) for num in X]
    print(' '.join(new))

        


if __name__ == "__main__":
    solve()
