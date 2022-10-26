# сложность алгоритма O(n), т.к мы проходим по циклу n раз

def numberOfMatches(n):
    matches = 0
    while n > 1:
        if n % 2 == 0:
            matches = matches + n/2
            n = n/2
        else:
            matches += (n - 1)/2
            n = (n - 1)/2 + 1
    return int(matches)


print(numberOfMatches(14))
