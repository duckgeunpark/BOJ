import sys

def solve() -> None:
    # .strip()을 추가하여 눈에 보이지 않는 공백과 줄바꿈(엔터)을 완벽하게 제거합니다.
    # 혹은 안전하게 N = int(input())만 사용해도 이 문제는 충분히 통과합니다.
    N = int(sys.stdin.readline().strip())
    
    L = 1  # 대각선 라인 번호
    
    # N이 속한 대각선 라인(L)과 해당 라인에서의 위치(N)를 찾음
    while N > L:
        N -= L
        L += 1
    
    # 짝수 라인: 분자 증가, 분모 감소
    if L % 2 == 0:
        X = N
        Y = L - N + 1
    # 홀수 라인: 분자 감소, 분모 증가
    else:
        X = L - N + 1
        Y = N

    # 정답 출력
    print(f"{X}/{Y}")
      
if __name__ == "__main__":
    solve()
