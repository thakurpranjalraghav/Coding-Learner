class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        filtered_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Use two-pointer approach
        left, right = 0, len(filtered_s) - 1
        while left < right:
            if filtered_s[left] != filtered_s[right]:
                return False
            left += 1
            right -= 1
        
        return True
