def searchInsert(nums: list, target: int):
    mid = round(len(nums)/2)
    while(mid != 1):
        if nums[mid] == target:
            return mid
        elif(nums[mid]<target):
            nums = nums[mid:]
        elif(nums[mid]>target):
            nums = nums[:mid]
        print(nums)
        mid = round(len(nums)/2)
    print(nums)
    return mid + 1



print(searchInsert([1,3,5,6,8],7))