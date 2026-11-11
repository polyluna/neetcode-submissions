class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        r = []
        for i in range (len(nums)):
            r.append(nums[i])
        for i in range (len(nums)):
            r.append(nums[i])
        return r
            