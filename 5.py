# сложность алгоритма O(n), т.к мы проходим по циклу n раз


def removeOuterParentheses(s):
    count = 0
    res = ''
    ind = 0
    for i in range(len(s)):
        if s[i] == '(':
            count = count + 1
        elif s[i] == ')':
            count = count - 1
        if count == 0:
            res = res + s[ind+1:i]
            ind = i+1
    return res

s = '(()())(())'
print(removeOuterParentheses(s))
