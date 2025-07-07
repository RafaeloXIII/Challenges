def strStr(haystack:str, needle:str):
    size_N = len(needle)
    temp = []
    for index in enumerate(haystack):
        if index + size_N > len(haystack):
            return -1
        for i in range(index, index+size_N):
            temp.append(haystack[i])
        string = ''.join(str(x) for x in temp)
        if string == needle:
            return index
        temp.clear()
    return -1 



print(strStr("sadbutsad","sad"))