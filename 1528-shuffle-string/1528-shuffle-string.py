class Solution(object):
    def restoreString(self, s, indices):
        result = [0] * len(s)
        for i in range(len(s)):
            result[indices[i]] = s[i]
        return "".join(result)


        