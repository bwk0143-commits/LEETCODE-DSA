from bisect import bisect_left, bisect_right


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        total_ones = s.count("1")
        n = len(s)

        # Maximal zero-runs: [start[i], end[i]]
        start, end, length = [], [], []
        i = 0

        while i < n:
            if s[i] == "1":
                i += 1
                continue

            left = i
            while i < n and s[i] == "0":
                i += 1

            right = i - 1
            start.append(left)
            end.append(right)
            length.append(right - left + 1)

        m = len(length)

        # pair_sum[i] = length of adjacent zero-runs i and i + 1.
        pair_sum = [length[i] + length[i + 1] for i in range(m - 1)]

        # Sparse table for range maximum queries on pair_sum.
        sparse = [pair_sum]
        level = 1

        while (1 << level) <= len(pair_sum):
            previous = sparse[-1]
            half = 1 << (level - 1)

            sparse.append([
                max(previous[i], previous[i + half])
                for i in range(len(previous) - half)
            ])
            level += 1

        def range_max(left: int, right: int) -> int:
            if left > right:
                return 0

            power = (right - left + 1).bit_length() - 1
            return max(
                sparse[power][left],
                sparse[power][right - (1 << power) + 1],
            )

        answer = []

        for query_left, query_right in queries:
            # First and last zero-runs that intersect this query.
            first = bisect_left(end, query_left)
            last = bisect_right(start, query_right) - 1

            gain = 0

            # A trade requires two zero-runs separated by a one-run.
            if first < m and last >= 0 and first < last:
                first_length = (
                    min(end[first], query_right)
                    - max(start[first], query_left)
                    + 1
                )
                last_length = (
                    min(end[last], query_right)
                    - max(start[last], query_left)
                    + 1
                )

                if first + 1 == last:
                    # Exactly two zero-runs intersect the query.
                    gain = first_length + last_length
                else:
                    # Pair containing the first clipped zero-run.
                    gain = max(gain, first_length + length[first + 1])

                    # Pair containing the last clipped zero-run.
                    gain = max(gain, length[last - 1] + last_length)

                    # Pairs entirely inside the query.
                    gain = max(gain, range_max(first + 1, last - 2))

            answer.append(total_ones + gain)

        return answer