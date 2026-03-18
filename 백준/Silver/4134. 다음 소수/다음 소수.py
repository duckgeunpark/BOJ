# BOJ 4134 - 다음 소수
# URL: https://www.acmicpc.net/problem/4134
# Tier: Silver IV
# Tags: 수학, 브루트포스 알고리즘, 정수론, 소수 판정

import sys
import math

input = sys.stdin.readline


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:  # 2는 위에서 처리, 1 이하는 False
        return False

    # 3부터 제곱근까지만 홀수만 확인 (속도 최적화)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def find_next_prime(n):
    # 0, 1의 경우 다음 소수는 2
    if n <= 2:
        return 2

    # 짝수면 다음 홀수부터 시작
    candidate = n if n % 2 == 1 else n + 1

    while not is_prime(candidate):
        candidate += 2

    return candidate


# 테스트 케이스 개수 입력 (한 번만!)
t = int(input())

for _ in range(t):
    num = int(input())
    print(find_next_prime(num))
