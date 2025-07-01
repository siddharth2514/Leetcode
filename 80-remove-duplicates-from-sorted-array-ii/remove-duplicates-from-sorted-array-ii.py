class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        count=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                count+=1
                if count>2:
                    del nums[i]
                else:
                    i+=1
            else:
                    i+=1
                    count=1  
        print(nums)                      




        
        