while True:
    arr = list(map(int, input().split()))
    if [0,0,0] == arr:
        break
    arr.sort()
    if arr[0] == arr[2]:
        print("Equilateral")
    elif arr[0] + arr[1] <= arr[2]:
        print("Invalid")
    elif arr[0] == arr[1] or arr[1] == arr[2]:
        print("Isosceles")
    else:
        print("Scalene")