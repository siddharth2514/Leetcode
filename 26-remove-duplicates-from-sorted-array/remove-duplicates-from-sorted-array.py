class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:]=list(set(nums))
        nums.sort()
        print(nums)
        