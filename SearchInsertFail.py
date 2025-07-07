def searchInsert(nums: list, target: int):
    original_nums = nums
    mid = round(len(nums)/2)
    while(len(nums) !=1):
        if nums[mid] == target:
            return mid
        elif(nums[mid]<target):
            nums = nums[mid:]
        elif(nums[mid]>target):
            nums = nums[:mid]
        print(nums)
        mid = round(len(nums)/2)
    if target > nums[0]: return(original_nums.index(nums[0])+1)
    return(original_nums.index(nums[0]))



print(searchInsert([2,7,8,9,10],9))