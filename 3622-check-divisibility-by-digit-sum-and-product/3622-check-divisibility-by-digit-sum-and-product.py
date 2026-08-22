class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        for i in str(abs(n)):
            s+=abs(int(i))
            p*=abs(int(i))
         
        if n%(s+p)==0:
            return True
        else:
            return False

        