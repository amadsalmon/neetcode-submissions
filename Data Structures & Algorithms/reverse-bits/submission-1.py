class Solution:
    def reverseBits(self, n: int) -> int:

        b = format(n, 'b')
        b = b.zfill(32)

        r = b[::-1]

        res = int(r, 2)

        return res
