class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t = list(t)

        for ch in s:
            if ch in t:
                t.remove(ch)
            else:
                return False

        return True