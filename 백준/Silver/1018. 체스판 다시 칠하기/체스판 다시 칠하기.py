import sys
input = sys.stdin.readline

def solve() -> None:
    # 1. 보드 크기 입력
    N, M = map(int, input().split())
    
    # 2. 보드 상태 입력받기 (이전에 배운 리스트 컴프리헨션 사용)
    board = [input().strip() for _ in range(N)]
    
    # 칠해야 하는 최솟값을 무한대(inf)로 초기화
    min_paint = float('inf')
    
    # 3. 8x8로 자를 수 있는 모든 시작점 (i, j) 탐색
    for i in range(N - 7):
        for j in range(M - 7):
            paint_W = 0  # 'W'로 시작할 때 칠해야 할 칸 수
            paint_B = 0  # 'B'로 시작할 때 칠해야 할 칸 수
            
            # 4. 자른 8x8 보드를 순회하며 검사
            for r in range(i, i + 8):
                for c in range(j, j + 8):
                    # 행 인덱스(r)와 열 인덱스(c)의 합이 짝수이면
                    # 시작점(i, j)과 같은 색상이어야 함
                    if (r + c) % 2 == 0:
                        if board[r][c] != 'W': paint_W += 1
                        if board[r][c] != 'B': paint_B += 1
                    # 합이 홀수이면 시작점과 다른 색상이어야 함
                    else:
                        if board[r][c] != 'B': paint_W += 1
                        if board[r][c] != 'W': paint_B += 1
            
            # 5. 현재 8x8 구역에서 가장 적게 칠하는 값을 갱신
            min_paint = min(min_paint, paint_W, paint_B)
            
    # 최종 결과 출력
    print(min_paint)

if __name__ == "__main__":
    solve()