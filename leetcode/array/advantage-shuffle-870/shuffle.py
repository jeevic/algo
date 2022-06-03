
# 暴利破解法
# 先排列获取所有可能形式
# 遍历排列元素比较求最优解


class Solution1:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 获取组合形式
        ag = self.arrange(nums1)
        best = 0
        besta = nums1
        for a in ag:
            b = self.compare(a, nums2)
            if b > best:
                besta = a
                best = b
        return besta

    def arrange(self, nums1):
        if len(nums1) == 1:
            return [nums1]
        result = []
        for i, v in enumerate(nums1):
            nums2 = nums1.copy()
            nums2.pop(i)
            r1 = [v]
            r = self.arrange(nums2)

            for rv in r:
                rc = r1.copy()
                rc.extend(rv)
                result.append(rc)

        return result

    def compare(self, a, nums2):
        counter = 0
        for (i, v) in enumerate(a):
            if a[i] > nums2[i]:
                counter += 1
        return counter


# 降序nums1
# 降薪nums2 保持索引关系
# 循环nums2 比较nums1对应大小 没有优势取nums1结尾小值
class Solution2:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 获取组合形式
        # nums1倒序
        nums1.sort(reverse=True)
        # nums2倒序排列
        nums2_sorted = sorted(enumerate(nums2), key=lambda x: x[1], reverse=True)

        result = [0 for i in range(len(nums1))]
        left = 0
        right = len(nums1) - 1
        for k, v  in nums2_sorted:
            if v >= nums1[left]:
                result[k] = nums1[right]
                right -= 1
            else:
                result[k] = nums1[left]
                left += 1
        return result