from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))

        values = [x[0] for x in arr]
        pos = [0] * n

        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        # right[i] = furthest sorted position reachable in one edge
        right = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
                j += 1
            right[i] = j

        LOG = n.bit_length()

        up = [right]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        def go_left():
            left = [0] * n
            j = n - 1
            for i in range(n - 1, -1, -1):
                while j - 1 >= 0 and values[i] - values[j - 1] <= maxDiff:
                    j -= 1
                left[i] = j
            return left

        left = go_left()

        down = [left]
        for _ in range(1, LOG):
            prev = down[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            down.append(cur)

        ans = []

        for u, v in queries:
            s = pos[u]
            t = pos[v]

            if s == t:
                ans.append(0)
                continue

            if s < t:
                cur = s
                steps = 0
                for k in range(LOG - 1, -1, -1):
                    nxt = up[k][cur]
                    if nxt < t:
                        cur = nxt
                        steps += 1 << k

                if right[cur] >= t:
                    ans.append(steps + 1)
                else:
                    ans.append(-1)

            else:
                cur = s
                steps = 0
                for k in range(LOG - 1, -1, -1):
                    nxt = down[k][cur]
                    if nxt > t:
                        cur = nxt
                        steps += 1 << k

                if left[cur] <= t:
                    ans.append(steps + 1)
                else:
                    ans.append(-1)

        return ans