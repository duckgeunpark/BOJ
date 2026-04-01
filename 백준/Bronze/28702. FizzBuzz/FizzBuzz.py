# BOJ 28702 - FizzBuzz
# URL: https://www.acmicpc.net/problem/28702
# Tier: Bronze I
# Tags: 수학, 문자열

import sys

input = sys.stdin.readline


def solve() -> None:
    a = input().strip()
    b = input().strip()
    c = input().strip()

    if a.isdigit():
        target = int(a) + 3
    elif b.isdigit():
        target = int(b) + 2
    elif c.isdigit():
        target = int(c) + 1

    if target % 3 == 0 and target % 5 == 0:
        print("FizzBuzz")
    elif target % 3 == 0:
        print("Fizz")
    elif target % 5 == 0:
        print("Buzz")
    else:
        print(target)


if __name__ == "__main__":
    solve()
