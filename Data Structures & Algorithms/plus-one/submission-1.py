class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits)))
        number += 1
        digit_list = [int(x) for x in str(number)]
        return digit_list