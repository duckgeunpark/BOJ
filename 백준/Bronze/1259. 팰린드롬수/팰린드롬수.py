import sys

input = sys.stdin.readline

def solve() -> None:
    while True:
        numbe = input().strip()
        if numbe == "0":
            break
        print("yes" if numbe == numbe[::-1] else "no")

if __name__ == "__main__":
    solve()
