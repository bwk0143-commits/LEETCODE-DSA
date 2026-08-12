class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=0
        k=[]
        for i in nums:
            c+=i
            k.append(c)
           
        return k
        