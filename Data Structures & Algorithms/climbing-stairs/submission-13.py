class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        for i in range(n-2):
            tmp = one
            one = two
            two = tmp + one
        return two  
 