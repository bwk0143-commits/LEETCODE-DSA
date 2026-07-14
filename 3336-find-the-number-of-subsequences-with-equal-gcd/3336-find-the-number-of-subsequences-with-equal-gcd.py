from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        m = max(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [[0] * (m + 1) for _ in range(m + 1)]

            for g1 in range(m + 1):
                for g2 in range(m + 1):
                    if dp[g1][g2] == 0:
                        continue

                    count = dp[g1][g2]

                    # Ignore x
                    new_dp[g1][g2] = (
                        new_dp[g1][g2] + count
                    ) % MOD

                    # Add x to seq1
                    ng1 = gcd(g1, x)
                    new_dp[ng1][g2] = (
                        new_dp[ng1][g2] + count
                    ) % MOD

                    # Add x to seq2
                    ng2 = gcd(g2, x)
                    new_dp[g1][ng2] = (
                        new_dp[g1][ng2] + count
                    ) % MOD

            dp = new_dp

        ans = 0

        for g in range(1, m + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans