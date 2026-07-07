class Solution:
    def sumAndMultiply(self, n: int) -> int:
        k=0
        l=0
        s=str(n)
        for i in s:
            d=int(i)
            if d!=0:
                l=l*10+d
                k+=d
        return k*l


        