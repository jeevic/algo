

def right_bound(nums, target:int) ->int:
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left - 1


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 6, 7, 8, 9]
    idx = right_bound(nums, 3)

    print(idx)
