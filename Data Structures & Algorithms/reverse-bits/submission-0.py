class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        b = bin(n)[2:]
        b = format(n, 'b')
        b = b.zfill(32)
        print(b)
        r = b[::-1]
        print(r)
        res = int(r, 2)
        print(res)

        return res
