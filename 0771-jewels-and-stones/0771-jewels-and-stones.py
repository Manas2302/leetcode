class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    count = count + 1
        return count        
        
        