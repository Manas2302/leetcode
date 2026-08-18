class Solution(object):
    def reverseWords(self, s):
        result = []
        words = s.split()
        for word in words:
            result.append(word[::-1])
        return " ".join(result)    

        