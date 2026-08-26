class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        positions = []

        
        for i, ch in enumerate(s):
            if ch == '1':
                positions.append(i)

        
        if len(positions) < k:
            return ""

        best = ""
        min_len = float('inf')

        
        for i in range(len(positions) - k + 1):
            left = positions[i]
            right = positions[i + k - 1]

            length = right - left + 1

            if length < min_len:
                min_len = length
                best = s[left:right + 1]

            elif length == min_len:
                candidate = s[left:right + 1]
                if candidate < best:
                    best = candidate

        return best