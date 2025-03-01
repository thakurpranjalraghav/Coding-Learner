class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # Negative numbers cannot be palindromes
            return False
        return str(x) == str(x)[::-1]  # Convert to string and compare with its reverse
