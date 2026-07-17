from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Step 1: Frequency of each number
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # Step 2: Count numbers divisible by each gcd
        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                cnt[g] += freq[multiple]

        # Step 3: Count pairs divisible by each gcd
        pairs = [0] * (mx + 1)
        for g in range(1, mx + 1):
            if cnt[g] >= 2:
                pairs[g] = cnt[g] * (cnt[g] - 1) // 2

        # Step 4: Inclusion-Exclusion
        # Keep only pairs whose gcd is exactly g
        for g in range(mx, 0, -1):
            multiple = 2 * g
            while multiple <= mx:
                pairs[g] -= pairs[multiple]
                multiple += g

        # Step 5: Prefix sums
        prefix = []
        total = 0
        for g in range(1, mx + 1):
            total += pairs[g]
            prefix.append(total)

        # Step 6: Answer queries
        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q) + 1)

        return ans