import sys
input = sys.stdin.readline

def solve() -> None:
    N = int(input())
    coins = [25, 10, 5, 1]

    for _ in range(N):
        C = int(input())
        res = []
        for coin in coins:
            res.append(C // coin)
            C %= coin
        print(*res)

if __name__ == "__main__":
    solve()
