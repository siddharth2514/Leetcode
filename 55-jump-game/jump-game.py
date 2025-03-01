from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Tracks the farthest index we can reach
        for i in range(len(nums)):
            if i > max_reach:  # If we reach a point that is not reachable
                return False
            max_reach = max(max_reach, i + nums[i])  # Update max reach
            if max_reach >= len(nums) - 1:  # If we can reach or pass the last index
                return True
        return False
