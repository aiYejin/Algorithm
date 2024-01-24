N = int(input())
arr = list(map(int, input().split()))
nums = [i for i in range(1, N+1)]

for i in range(N-1, -1, -1):
    nums.insert(i+arr[i]+1, nums[i])
    del nums[i]
for n in nums:
    print(n, end=' ')