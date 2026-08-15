class Solution:
    def fib(self, n: int) -> int:
        f=0
        f2=0
        f1=1
        i=0
        while i<n:
            f=f1+f2
            f1=f2
            f2=f
            i+=1
        return f

            
        