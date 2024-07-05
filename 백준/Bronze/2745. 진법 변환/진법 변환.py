def convert_to_decimal(N, B):
    return int(N, B)

# 입력 받기
N, B = input().split()
B = int(B)

# 10진법으로 변환하여 출력
print(convert_to_decimal(N, B))