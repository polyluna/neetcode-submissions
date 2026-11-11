class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            new_s = s
            for i in range(len(t)):
                new_s = new_s.replace(t[i], "", 1)
            return len(new_s) == 0
            