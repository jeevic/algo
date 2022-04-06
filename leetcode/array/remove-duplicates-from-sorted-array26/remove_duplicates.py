from typing import List

# @see https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        i = 0
        end = len(nums)
        while i < end:
            val = nums[i]
            while i < end - 1 and nums[i + 1] == val:
                self.delAndMove(nums, i+1, end - 1)
                end = end - 1
            i = i + 1
            length = length + 1

        return length

    def delAndMove(self, nums, index, end: int):
        while index < end:
            nums[index] = nums[index + 1]
            index = index + 1


# 快慢指针法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head = 0
        last = 1
        length = len(nums)

        while last < length:
            if nums[last] != nums[head] and last - head > 1:
                head = head + 1
                nums[head] = nums[last]
            last = last + 1
        return head + 1


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    print(s.removeDuplicates(nums))
