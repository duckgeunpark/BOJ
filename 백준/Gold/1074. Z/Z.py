# BOJ 1074 - Z
# URL: https://www.acmicpc.net/problem/1074
# Tier: Gold V
# Tags: 분할 정복, 재귀

import sys

input = sys.stdin.readline


def solve() -> None:
    N, r, c = map(int, input().split())
    count = 0

    while N != 0:
        N -= 1
        half = 2**N
        if r < half and c < half:  # 4등분 한것중 첫번째 박스에 있는지 확인
            count += (half * half) * 0

        elif r < half and c >= half:  # 4등분 한것중 두번째 박스에 있는지 확인
            count += (half * half) * 1
            c -= half  # 다음 탐색을 위해 기준점 변경

        elif r >= half and c < half:  # 4등분 한것중 세번째 박스에 있는지 확인
            count += (half * half) * 2
            r -= half  # 다음 탐색을 위해 기준점 변경

        else:  # 4등분 한것중 네번째 박스에 있는지 확인
            # 카운터 수는 제일작은 박스 기준 4개 16개 .. -> 2**n(짝수) 수 만큼 그냥 더함
            count += (half * half) * 3
            # 다음 탐색을 위해 기준점 변경
            r -= half
            c -= half

    print(count)


if __name__ == "__main__":
    solve()
