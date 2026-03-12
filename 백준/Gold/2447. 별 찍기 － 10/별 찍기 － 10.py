# BOJ 2447 - 별 찍기 - 10
# URL: https://www.acmicpc.net/problem/2447
# Tier: Gold V
# Tags: 분할 정복, 재귀

import sys
input = sys.stdin.readline

def draw_stars(n: int) -> list:
    if n == 1:
        return ['*']
    stars = draw_stars(n // 3)
    L = []

    for star in stars:
        L.append(star * 3)
    for star in stars:
        L.append(star + ' ' * (n // 3) + star)
    for star in stars:
        L.append(star * 3)
        
    return L

def solve() -> None:
    num = int(input())
    
    result = draw_stars(num)
    print('\n'.join(result))

if __name__ == "__main__":
    solve()