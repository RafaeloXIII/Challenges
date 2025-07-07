def searchInsert(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If not found, left will be the correct insertion point
    return left

# Examples
print(searchInsert([1,3,5,6], 5))
