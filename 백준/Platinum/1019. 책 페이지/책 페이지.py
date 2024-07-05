def count_digits(N):
    counts = [0] * 10
    factor = 1
    while factor <= N:
        lower_numbers = N - (N // factor) * factor
        current_digit = (N // factor) % 10
        higher_numbers = N // (factor * 10)
        
        for i in range(10):
            counts[i] += higher_numbers * factor
        
        for i in range(current_digit):
            counts[i] += factor
        
        counts[current_digit] += lower_numbers + 1
        
        counts[0] -= factor
        factor *= 10
    
    return counts

# 입력 받기
N = int(input())

# 각 숫자의 출현 횟수 계산
result = count_digits(N)

# 결과 출력
print(" ".join(map(str, result)))