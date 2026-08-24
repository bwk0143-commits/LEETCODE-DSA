class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        # Prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # If there are n stones, the final possible move
        # takes all n stones.
        ans = prefix[n - 1]

        # Try states where the current player has compressed
        # the first i stones into prefix[i].
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans