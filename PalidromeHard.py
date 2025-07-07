def isPalindrome(x):
    if x < 0:
        False
    num_list = []
    pivot = x
    while pivot != 0:
        num_list.append(pivot%10)
        pivot = round(pivot/10)
    if num_list == num_list[::-1]:
        print("ok")

isPalindrome(122)