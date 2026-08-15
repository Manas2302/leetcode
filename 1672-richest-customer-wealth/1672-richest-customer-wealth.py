class Solution(object):
    def maximumWealth(self, accounts):
        result = 0
        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[i])):
                 total += accounts[i][j]
            
       
            if total > result:
               result = total
        return result

        