class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=[]
        c=0
        for i in nums:
            if i!=0:
                c+=1
            else:
                c=0
            k.append(c)
        return max(k)
            
        