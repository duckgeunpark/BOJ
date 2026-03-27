# BOJ 10828 - 스택
# URL: https://www.acmicpc.net/problem/10828
# Tier: Silver IV
# Tags: 구현, 자료 구조, 스택


import sys

input = sys.stdin.readline

stack = []


def commend(cmd: str, n: int = 0):
    if cmd == "push":
        stack.append(n)
        return None  # 출력 없음
    elif cmd == "pop":
        return stack.pop() if stack else -1
    elif cmd == "size":
        return len(stack)
    elif cmd == "empty":
        return 0 if stack else 1
    elif cmd == "top":
        return stack[-1] if stack else -1


def solve() -> None:
    n = int(input())
    result = []

    for i in range(n):
        Aa = input().split()
        cmd = Aa[0]
        b = int(Aa[1]) if len(Aa) > 1 else 0
        anser = commend(cmd, b)
        if anser is not None:
            result.append(str(anser))

    print("\n".join(result))


if __name__ == "__main__":
    solve()
