from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element mapping
        next_greater = {}
        stack = []  # Monotonic decreasing stack
        
        # Iterate over nums2 to find the next greater element for each number
        for num in nums2:
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            stack.append(num)
        
        # Remaining numbers in stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Generate the output list for nums1 based on the next_greater mapping
        return [next_greater[num] for num in nums1]
