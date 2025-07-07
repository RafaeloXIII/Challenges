def isValid(str):
    stack = []
    open_list = ['(','[','{']
    close_list = [')',']','}']
    for c in str:
        if c in open_list:
            stack.append(c)
            print(stack)
        else:
            value = close_list.index(c)
            try:
                if open_list[value] in stack[-1]:
                    stack.pop()
                else:
                    return False
            except:
                return False
    if stack == []:
        return True
    return False

print(isValid("()"))