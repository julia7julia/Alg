# сложность алгоритма O(n), т.к мы проходим по циклу n раз

def numJewelsInStones(jewels, stones):
    jewel = set(jewels)
    count_of_jewel = 0
    for item in stones:
        if item in jewel:
            count_of_jewel = count_of_jewel + 1

    return count_of_jewel


jewels = 'aA'
stones = 'aAAbbbb'
print(numJewelsInStones(jewels, stones))
