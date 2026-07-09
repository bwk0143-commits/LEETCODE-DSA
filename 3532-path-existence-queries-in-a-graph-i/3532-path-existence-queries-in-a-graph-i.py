class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        comp = [0] * n

        for i in range(1, n):
            comp[i] = comp[i - 1]
            if nums[i] - nums[i - 1] > maxDiff:
                comp[i] += 1

        return [comp[u] == comp[v] for u, v in queries]