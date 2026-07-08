from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Prefix sum of digits
        pref_sum = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref_sum[i + 1] = pref_sum[i] + int(ch)

        # Non-zero positions and digits
        pos = []
        digits = []
        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        m = len(digits)

        # Powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix value of non-zero digit sequence
        pref_val = [0] * (m + 1)
        for i in range(m):
            pref_val[i + 1] = (pref_val[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (pref_val[right + 1] -
                 pref_val[left] * pow10[length]) % MOD

            digit_sum = pref_sum[r + 1] - pref_sum[l]

            ans.append((x * digit_sum) % MOD)

        return ans