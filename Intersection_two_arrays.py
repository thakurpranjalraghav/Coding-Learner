from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)  # Count occurrences in nums1
        count2 = Counter(nums2)  # Count occurrences in nums2
        
        intersection = []
        for num in count1:
            if num in count2:
                intersection.extend([num] * min(count1[num], count2[num]))  # Add the minimum count
        
        return intersection
