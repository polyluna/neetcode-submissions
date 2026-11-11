class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if ((n>>i) & 1):
                res |= (1 << (31-i))
            else:
                res |= (0 << (31-i))
        return res