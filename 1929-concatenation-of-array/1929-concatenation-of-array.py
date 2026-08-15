class Solution(object):
    def getConcatenation(self, nums):
        result = []
        for i in range(len(nums)):
            result.append(nums[i])
        for j in range(len(nums)):
            result.append(nums[j])
        return result