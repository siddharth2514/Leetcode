class Solution:
    def majorityElement(self, nums: List[int]) -> int:
     max_frequency=max(set(nums),key=nums.count)
     return max_frequency

       