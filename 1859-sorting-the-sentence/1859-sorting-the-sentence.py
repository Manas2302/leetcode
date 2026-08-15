class Solution(object):
    def sortSentence(self, s):
        result = []
        words = s.split()
        words = sorted(words, key=lambda word: int(word[-1]))
        for word in words:
            result.append(word[:-1])
        return " ".join(result)
