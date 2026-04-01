# BOJ 11723 - 집합
# URL: https://www.acmicpc.net/problem/11723
# Tier: Silver V
# Tags: 구현, 집합과 맵, 비트마스킹

import sys

input = sys.stdin.readline


import sys
input = sys.stdin.readline

def solve() -> None:
    m = int(input())
    S = set()
    for _ in range(m):
        command = input().split()
        cmd = command[0]
        
        if cmd == "all":
            S = set(range(1, 21))  # 정수가 들어감
        elif cmd == "empty":
            S.clear()
        else:
            x = int(command[1])    # 💡 문자열을 정수로 변환!
            
            if cmd == "add":
                S.add(x)
            elif cmd == "remove":
                S.discard(x)
            elif cmd == "check":
                print(1 if x in S else 0)
            elif cmd == "toggle":
                if x in S:
                    S.discard(x)
                else:
                    S.add(x)

if __name__ == "__main__":
    solve()
