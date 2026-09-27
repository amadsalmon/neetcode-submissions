class Solution:
    def largestGoodInteger(self, s: str) -> str:
        i = 0
        maxIntFound = -1
        maxStrFound = ""
        while i < len(s)-2:
            if s[i] == s[i+1] and s[i] == s[i+2] :
                if int(s[i]) > maxIntFound:
                    maxIntFound = int(s[i])
                    maxStrFound = s[i:i+3]
            i += 1
        return maxStrFound
        