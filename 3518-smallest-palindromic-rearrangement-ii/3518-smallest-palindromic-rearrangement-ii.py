from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [x // 2 for x in freq]
        middle = ""
        for i in range(26):
            if freq[i] % 2:
                middle = chr(ord('a') + i)

        def count_ways(counts, limit):
            result = 1
            remaining = sum(counts)

            for cnt in counts:
                if cnt == 0:
                    continue

                result *= comb(remaining, cnt)
                if result >= limit:
                    return limit
                remaining -= cnt

            return result

        if count_ways(half, k) < k:
            return ""

        left = []

        for _ in range(len(s) // 2):
            for ch in range(26):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count_ways(half, k)

                if ways >= k:
                    left.append(chr(ord('a') + ch))
                    break

                k -= ways
                half[ch] += 1

        left = "".join(left)
        return left + middle + left[::-1]