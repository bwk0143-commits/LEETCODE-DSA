class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ns=set(nums)
        m=k
        while m in ns:
            m+=k
        return m