def removeDuplicates(nums: list, val:int):
    write = len(nums)-1
    index = 0
    while(index <= write):
            if nums[write] == val:
                write -=1
                continue
            if nums[index] == val:
                nums[index],nums[write] = nums[write],nums[index]
                write -=1
            index +=1
    return write + 1



print(removeDuplicates([1,2,4,1,1,1,1,3,3,1,1,2,4,3],1))