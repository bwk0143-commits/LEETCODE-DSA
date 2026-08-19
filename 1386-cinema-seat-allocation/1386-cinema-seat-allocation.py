from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store only seats that matter: 2 to 9
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                rows.setdefault(r, set()).add(s)

        # Every completely empty row can fit 2 groups
        ans = 2 * (n - len(rows))

        for seats in rows.values():
            left = all(s not in seats for s in [2, 3, 4, 5])
            middle = all(s not in seats for s in [4, 5, 6, 7])
            right = all(s not in seats for s in [6, 7, 8, 9])

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans