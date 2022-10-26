# сложность алгоритма O(n), т.к мы проходим по циклу n раз

def sumBase(n, k):
    number = 0
    while n != 0:
        number = number + n % k
        n = n // k
    return number


n = 34
k = 6

print(sumBase(n, k))
