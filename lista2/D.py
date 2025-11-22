n = int(input())
for i in range(1, n+1):
    v1 = "⠀"*((n - i)+1)
    v2 = "#"*(2*i-1)
    print(v1 + v2)