class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            # Update the current element with the sum of itself and the previous element
            nums[i] += nums[i - 1]
        # Return the modified array
        return nums
