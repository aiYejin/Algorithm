def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)
def lcm(a, b):
    return a*b//gcd(a, b)
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A,B))