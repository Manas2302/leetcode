class Solution(object):
    def sumOfUnique(self, nums):
        count = {}
        result = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in count:
            if count[num] == 1:
                result += num
        return result       
      
    

        
        