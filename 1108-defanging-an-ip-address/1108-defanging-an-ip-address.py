class Solution(object):
    def defangIPaddr(self, address):
        result = []
        for i in range(len(address)):
            if address[i] == ".":
                result.append("[.]")
            else:
                result.append(address[i])  
        return "".join(result)        

        