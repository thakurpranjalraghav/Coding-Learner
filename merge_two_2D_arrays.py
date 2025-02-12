from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        id_map = {}  # Dictionary to store id -> sum of values
        
        # Add values from nums1
        for id, val in nums1:
            id_map[id] = id_map.get(id, 0) + val
        
        # Add values from nums2
        for id, val in nums2:
            id_map[id] = id_map.get(id, 0) + val
        
        # Convert dictionary to a sorted list
        result = [[id, val] for id, val in sorted(id_map.items())]
        
        return result
