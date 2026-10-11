class Solution:

    def longestPalindrome(self, s: str) -> str:
        max_found = ""

        # Checking odd-length palindromes
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                current_substring = s[l:r+1]
                if s[l] == s[r]:
                    if len(current_substring) > len(max_found):
                        max_found = current_substring
                else:
                    break

                l -= 1
                r += 1
        
        # Now checking even-length palindromes
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s):
                current_substring = s[l:r+1]
                if s[l] == s[r]:
                    if len(current_substring) > len(max_found):
                        max_found = current_substring
                else:
                    break
                l -= 1
                r += 1
        
        return max_found


    """
    O(N^3) solution below, errors in Time Limit Exceeded for large input
    """
    def longestPalindrome_brute(self, s: str) -> str:
        
        def isPalindrome(s: str) -> bool:
            if len(s) <= 1:
                return True

            if s[0] != s[-1]:
                return False

            return isPalindrome(s[1:-1])

        max_found = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    if len(s[i:j+1]) > len(max_found):
                        max_found = s[i:j+1]
        
        return max_found

