class Solution:
    def containsDuplicate(self, nums: List[int]) ->bool:
        c=0
        n=set()
        for i in nums:
            if i in n:
                return True
            n.add(i)   
        return False
            
        