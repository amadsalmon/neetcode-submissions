class Solution:
    def isPalindrome_0(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]
        
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        n = len(x_str)
        for i in range(int(n/2)):
            if x_str[i] != x_str[n-i-1]: return False
        return True