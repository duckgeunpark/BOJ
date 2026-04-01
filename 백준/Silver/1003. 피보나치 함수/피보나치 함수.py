# BOJ 1003 - 피보나치 함수
# URL: https://www.acmicpc.net/problem/1003
# Tier: Silver III
# Tags: 다이나믹 프로그래밍

import sys

input = sys.stdin.readline


def solve() -> None:
    # 1. 0과 1의 호출 횟수를 저장할 DP 테이블 (N은 최대 40)
    dp0 = [0] * 41
    dp1 = [0] * 41

    # 2. 초기값 세팅 (N=0, N=1일 때)
    dp0[0], dp1[0] = 1, 0
    dp0[1], dp1[1] = 0, 1

    # 3. N=40까지 미리 피보나치 규칙으로 계산해둠
    for i in range(2, 41):
        dp0[i] = dp0[i - 1] + dp0[i - 2]
        dp1[i] = dp1[i - 1] + dp1[i - 2]

    # 4. 입력받은 수에 맞춰 정답 출력
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dp0[n], dp1[n])


if __name__ == "__main__":
    solve()
