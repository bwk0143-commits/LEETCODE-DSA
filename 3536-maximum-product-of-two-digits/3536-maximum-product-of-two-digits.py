class Solution:
    def maxProduct(self, n: int) -> int:
        k=[]
        a=str(n)
        for i in a:
            k.append(int(i))
        k.sort()
        return k[-1]*k[-2]