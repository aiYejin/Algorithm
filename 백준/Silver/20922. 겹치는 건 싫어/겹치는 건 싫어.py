N, K = map(int, input().split())
arr = list(map(int, input().split()))
counter = [0] * (max(arr)+1)
answer = 0
right, left = 0, 0

while right < N:
    if counter[arr[right]] < K:
        counter[arr[right]] += 1
        right += 1
        answer = max(answer, right - left)
    else:
        counter[arr[left]] -= 1
        left += 1
print(answer)