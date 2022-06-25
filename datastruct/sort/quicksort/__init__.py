

class QuickSort:

    def __init__(self):
        pass

    def sort(self, nums):
        length = len(nums)
        if length <= 1:
            return nums
        self.sorted(nums, 0, length - 1)
        return nums

    @classmethod
    def sorted(cls, nums, lo, hi):
        if lo >= hi:
            return
        mid = QuickSort.partition(nums, lo, hi)

        QuickSort.sorted(nums, lo, mid - 1)
        QuickSort.sorted(nums, mid + 1, hi)

        return

    @classmethod
    def partition(cls, nums, lo, hi):
        mid = lo + (hi - lo) // 2
        # get less than nums
        i = lo
        lc = 0
        while i <= hi:
            if nums[i] <= nums[mid]:
                lc += 1
            i += 1

        last_mid = lo + lc - 1
        nums[mid], nums[last_mid] = nums[last_mid], nums[mid]
        mid = last_mid

        start = lo
        end = hi

        while start < mid:
            if nums[start] > nums[mid]:
                while nums[end] > nums[mid]:
                    end -= 1
                nums[start], nums[end] = nums[end], nums[start]

            start += 1
        return mid


if __name__ == '__main__':
    arr = [1, 3, 4, 2, 6, 7, 9, 8, 8, 2]

    print(QuickSort().sort(arr))
