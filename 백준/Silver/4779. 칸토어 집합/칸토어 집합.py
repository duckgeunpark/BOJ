# BOJ 4779 - 칸토어 집합
# URL: https://www.acmicpc.net/problem/4779
# Tier: Silver III
# Tags: 분할 정복, 재귀

import sys
input = sys.stdin.readline

def cantor(n: int) -> str:
    if n == 0:
        return "-"
    prev = cantor(n - 1)
    spaces = " " * (3 ** (n - 1))
    return prev + spaces + prev
  
def solve() -> None:
    while True:
        try:
            line = input().strip()
            if not line:
                break   
            n = int(line)
            print(cantor(n))
        except EOFError:
            break 

if __name__ == "__main__":
    solve()
