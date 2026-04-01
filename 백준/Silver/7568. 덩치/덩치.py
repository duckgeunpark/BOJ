# BOJ 7568 - 덩치
# URL: https://www.acmicpc.net/problem/7568
# Tier: Silver V
# Tags: 구현, 브루트포스 알고리즘

import sys

input = sys.stdin.readline


def solve() -> None:
    ans = []
    rank = []
    n = int(input())
    for _ in range(n):
        ans.append(list(map(int, input().split())))

    for i in range(n):
        myrank = 1  # 1. 기본 등수를 1등으로 시작
        for j in ans:
            # 2. 나보다 덩치가 확실히 큰 사람을 만나면 등수가 밀려남
            if ans[i][0] < j[0] and ans[i][1] < j[1]:
                myrank += 1
        rank.append(myrank)  # 3. ans가 아닌 rank에 등수 추가

    print(*rank)


if __name__ == "__main__":
    solve()
