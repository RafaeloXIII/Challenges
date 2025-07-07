def longestCommonPrefix(strs: list):
    output = ""
    
    for x in range(len(strs[0])):
        try:
            char_list = [string[x] for string in strs]
            if all(c == char_list[0] for c in char_list):
                output += char_list[0]
        except:
            break
    return output

                


print(longestCommonPrefix(["flower","flow","flight"]))