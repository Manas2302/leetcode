class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        result = []

        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        all_nums = set1 | set2 | set3
        for num in all_nums:
            count = 0

            if num in set1:
                count += 1
            if num in set2:
                count += 1
            if num in set3:
                count += 1
            if count  >= 2:
                result.append(num)

        return result            
    