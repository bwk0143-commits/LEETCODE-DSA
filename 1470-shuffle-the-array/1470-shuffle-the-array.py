class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k=[]
        for i in range(n):
            k.append(nums[i])
            k.append(nums[i+n])
        return k