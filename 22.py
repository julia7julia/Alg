# сложность алгоритма O(n), т.к мы проходим по циклу n раз
def getMaximumGenerated(n):
    if n == 0:
        return 0
    arr = [0, 1]
    for i in range(2, n + 1):
        if i % 2 == 0:
            arr.append(arr[i // 2])
        else:
            arr.append(arr[i // 2] + arr[i // 2 + 1])
    return max(arr)


print(getMaximumGenerated(7))

