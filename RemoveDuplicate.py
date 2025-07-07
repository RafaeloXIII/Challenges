def removeDuplicates(nums: list):
    write = 1
    for index in range(1,len(nums)):
        if nums[index] != nums[index-1]:
            nums[write] = nums[index]
            write +=1
    return write



print(removeDuplicates([1,1,2]))