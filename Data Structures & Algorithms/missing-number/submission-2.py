class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myset = set(range(0,len(nums)+1))
        
        for x in nums:
            myset.remove(x)

        return myset.pop()