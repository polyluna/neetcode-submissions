class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_dict = {}

        for key, value in enumerate(nums):
            if value in my_dict:
                return [my_dict[value], key]
            else:
                my_dict[target - value] = key
        
        return []