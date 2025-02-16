from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # First row always starts with 1
        
        for i in range(rowIndex):  # Generate rowIndex rows
            row.append(1)  # Add 1 at the end
            for j in range(len(row) - 2, 0, -1):  # Update from right to left
                row[j] += row[j - 1]
        
        return row
