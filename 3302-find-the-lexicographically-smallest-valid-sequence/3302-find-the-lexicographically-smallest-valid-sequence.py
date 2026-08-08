class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # e0[i] = maximum number of suffix characters of word2
        # that can be matched exactly using word1[i:].
        e0 = [0] * (n + 1)

        # e1[i] = maximum number of suffix characters of word2
        # that can be matched using at most one mismatch in word1[i:].
        e1 = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Exact match
            if e0[i + 1] < m and word1[i] == word2[m - 1 - e0[i + 1]]:
                e0[i] = e0[i + 1] + 1
            else:
                e0[i] = e0[i + 1]

            # At most one mismatch
            match = e1[i + 1]

            if match < m and word1[i] == word2[m - 1 - match]:
                match += 1

            # Use the one allowed mismatch at word1[i]
            mismatch = min(m, e0[i + 1] + 1)

            e1[i] = max(match, mismatch)

        ans = []
        pos = 0
        used_mismatch = False

        for i in range(m):
            remaining = m - i - 1
            found = False

            while pos < n:
                # Case 1: current character matches
                if word1[pos] == word2[i]:
                    if used_mismatch:
                        possible = e0[pos + 1] >= remaining
                    else:
                        possible = e1[pos + 1] >= remaining

                    if possible:
                        ans.append(pos)
                        pos += 1
                        found = True
                        break

                # Case 2: use the one allowed mismatch here
                elif not used_mismatch and e0[pos + 1] >= remaining:
                    ans.append(pos)
                    pos += 1
                    used_mismatch = True
                    found = True
                    break

                pos += 1

            if not found:
                return []

        return ans