class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decode(start_index: int) -> int:
            if start_index >= len(s):
                return 1
            if s[start_index] == '0':
                return 0
            
            if s[start_index:] in memo:
                return memo[s[start_index:]]
            
            memo[s[start_index:]] = decode(start_index + 1)
            
            if (start_index + 1 < len(s)) and int(s[start_index : start_index + 2]) <= 26:
                memo[s[start_index:]] += decode(start_index + 2)
                
            return memo[s[start_index:]] 

        return decode(0)

