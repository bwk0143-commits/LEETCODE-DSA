class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j]:
                    c+=1
            if c>len(nums)/2:
                return nums[i]
            

        