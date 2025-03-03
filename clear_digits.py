class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()  # Remove closest non-digit to the left
            else:
                stack.append(char)  # Store non-digits
        
        return "".join(stack)
