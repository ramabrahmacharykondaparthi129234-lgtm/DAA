n = int(input("Enter number of items: "))

w = list(map(int, input("Enter weights: ").split()))
p = list(map(int, input("Enter profits: ").split()))

W = int(input("Enter capacity: "))

M = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(W + 1):
        if w[i - 1] <= j:
            M[i][j] = max(M[i - 1][j],
                           M[i - 1][j - w[i - 1]] + p[i - 1])
        else:
            M[i][j] = M[i - 1][j]

print("Maximum profit:", M[n][W])
