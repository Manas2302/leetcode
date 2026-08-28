class Solution(object):
    def isIsomorphic(self, s, t):
        mapping = {}
        reverse_mapping = {}
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            if t[i] in reverse_mapping:
                if reverse_mapping[t[i]] != s[i]:
                    return False   
            
            mapping[s[i]] = t[i]
            reverse_mapping[t[i]] = s[i]

        return True
               
                      