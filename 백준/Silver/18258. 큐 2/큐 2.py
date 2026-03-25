# BOJ 18258 - 큐 2
# URL: https://www.acmicpc.net/problem/18258
# Tier: Silver IV
# Tags: 자료 구조, 큐

import sys

from collections import deque  # list.pop(0) 빠르기 위해

input = sys.stdin.readline

nums = deque()

n = int(input())
for _ in range(n):
    cmd = input().split()  # ['push', '123'] 또는 ['pop']
    order = cmd[0]

    if order == "push":
        nums.append(int(cmd[1]))
    elif order == "pop":
        print(nums.popleft() if nums else -1)
    elif order == "size":
        print(len(nums))
    elif order == "empty":
        print(0 if nums else 1)
    elif order == "front":
        print(nums[0] if nums else -1)
    elif order == "back":
        print(nums[-1] if nums else -1)
