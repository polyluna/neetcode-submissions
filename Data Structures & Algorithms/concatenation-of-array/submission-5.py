class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        r = []
        for j in range(2):
            for i in nums:
             r.append(i)
        
        return r
            