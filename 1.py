# сложность алгоритма O(n), т.к мы проходим по циклу n раз

def numberOfSteps(number):
    count = 0
    while number != 0:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number - 1
        count = count + 1

    return count


print(numberOfSteps(123))
