from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        f=Counter(word)
        arr=sorted(f.values(),reverse=True)
        a=0
        for i,f in enumerate(arr):
            cost=(i//8)+1
            a+=f*cost
        return a
            
        return a
        

        