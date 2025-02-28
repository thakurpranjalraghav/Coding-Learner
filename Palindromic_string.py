class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:  # Check if the word is a palindrome
                return word  # Return the first palindrome found
        return ""  # Return empty string if no palindrome is found
