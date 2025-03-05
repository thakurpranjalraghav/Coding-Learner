class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0  # Balance to track depth of parentheses
        
        for char in s:
            if char == '(':
                if balance > 0:  # Ignore outermost '('
                    result.append(char)
                balance += 1
            else:  # char == ')'
                balance -= 1
                if balance > 0:  # Ignore outermost ')'
                    result.append(char)
        
        return "".join(result)
