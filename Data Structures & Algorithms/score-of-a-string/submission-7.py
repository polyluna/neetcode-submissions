class Solution:
    def scoreOfString(self, s: str) -> int:
        num = []
        rsf = 0
        for i in range(len(s)): 
            num.append(ord(s[i]))
        for i in range(len(s)): 
            if i == 0:
                pass
            else:
                rsf += abs(num[i] - num[i-1])

        return rsf