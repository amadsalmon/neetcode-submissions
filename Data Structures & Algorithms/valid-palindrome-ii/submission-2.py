class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValidPalindrome(left: int, right: int) -> bool:
            while left <= right:
                if not s[left] == s[right]:
                    return False
                left += 1
                right -= 1
            return True


        l, r = 0, len(s) - 1
        while l <= r:
            if not s[l] == s[r]:
                return isValidPalindrome(l + 1, r) or isValidPalindrome(l, r - 1)
             
            l += 1
            r -= 1

        return True
