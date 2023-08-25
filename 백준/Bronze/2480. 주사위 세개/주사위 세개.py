num = list(map(int, input().split()))
if max(num)==min(num):
    print(10000+max(num)*1000)
elif sum(num)-max(num)==min(num)*2:
    print(1000+min(num)*100)
elif sum(num)-min(num)==max(num)*2:
    print(1000+max(num)*100)
else:
    print(max(num)*100)