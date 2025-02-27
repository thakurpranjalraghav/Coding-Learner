from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])  # Start with the first array as a set
        for arr in nums[1:]:   # Iterate through the remaining arrays
            result.intersection_update(arr)  # Keep only common elements
        return sorted(result)  # Return the sorted list of common elements
