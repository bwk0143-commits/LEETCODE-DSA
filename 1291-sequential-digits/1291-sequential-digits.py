class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a=[]
        for i in range(1,10):
            n=i
            for j in range(i+1,10):
                n=n*10+j
                if low<=n<=high:
                    a.append(n)
                if n>high:
                    break
        
        a.sort()
        return a
        