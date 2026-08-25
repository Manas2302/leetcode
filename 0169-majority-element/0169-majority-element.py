class Solution(object):
    def majorityElement(self, nums):
        for i in range(len(nums)):
            count = {}
            for num in nums:
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1
            for num in count:
                if count[num] > len(nums) / 2:
                    return num

                





        