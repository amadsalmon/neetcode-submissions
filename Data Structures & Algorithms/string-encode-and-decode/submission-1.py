SEP = '#'

class Solution:
    
    """
    Encode:
    Init empty string res = ""
    Iterate over each string. For each, compute its length. So you add to res: length(s)+SEP+s
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + SEP + s
        return res

    """
    Init empty string array res = ""
    iterate while s is not empty:
    get next length : get all numbers until you hit SEP → l
    grab s[:l], append that to res, replace s with the slice after that.
    return res
    """
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != SEP:
                j += 1
            
            length = int(s[i:j])

            word = s[j+1:j+length+1]
            res.append(word)
            i = j+length+1

        return res

