
def romanToInt(s):
    roman = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    skip = False
    total = 0
    for index, character in enumerate(s): 
        print(character)
        if skip == True:
            skip = False
            print("skip")
            continue
        if index + 1 < len(s):
            s_temp = s[index] + s[index + 1] 
            if s_temp in roman:
                print("in")
                skip = True
                total += roman[s_temp]
            else:
                total += roman[s[index]]
        if index + 1 == len(s):
            total += roman[s[index]]         
    return total

print(romanToInt("MCD"))