
def pascal_triangle(n):
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = [0 for _ in range(i + 1)]
        arr[i][0] = 1
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
            print(f'arr{i,j} = arr{i - 1,j - 1} + arr{i - 1,j}')

        arr[i][i] = 1

    return arr


print(pascal_triangle(5))
