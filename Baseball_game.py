from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []  # Stack to store valid scores
        
        for op in operations:
            if op == "C":  # Remove last score
                record.pop()
            elif op == "D":  # Double last score
                record.append(2 * record[-1])
            elif op == "+":  # Sum of last two scores
                record.append(record[-1] + record[-2])
            else:  # It's a valid integer, convert and add
                record.append(int(op))
        
        return sum(record)  # Return total sum
