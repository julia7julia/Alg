# сложность алгоритма O(n), т.к мы проходим по циклу n раз
def rob(nums):
    a = len(nums)
    if a == 0:
        return 0
    if a <= 3:
        return max(nums)
    b, c, d, e = nums[1], nums[0], nums[2], nums[0] + nums[2]
    for n in range(3, a):
        b, c, d, e = max(b, d), max(c, e), b + nums[n], c + nums[n]
    return max(b, c, d)


print(rob([1, 2, 3, 1]))
