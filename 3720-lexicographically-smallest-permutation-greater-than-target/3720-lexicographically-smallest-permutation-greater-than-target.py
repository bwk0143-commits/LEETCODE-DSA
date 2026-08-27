class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Try to follow target
        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            # Exact character available
            if cnt[t] > 0:
                cnt[t] -= 1
                continue

            # Cannot match target[i].
            # Make this position greater.
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    ans = target[:i] + chr(c + ord('a'))

                    for j in range(26):
                        ans += chr(j + ord('a')) * cnt[j]

                    return ans

            # No greater character here.
            break

        # Need to backtrack.
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for i in range(len(target) - 1, -1, -1):

            # Build target prefix [0, i)
            ok = True

            for j in range(i):
                c = ord(target[j]) - ord('a')

                if cnt[c] == 0:
                    ok = False
                    break

                cnt[c] -= 1

            if ok:
                t = ord(target[i]) - ord('a')

                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        cnt[c] -= 1

                        ans = target[:i] + chr(c + ord('a'))

                        for j in range(26):
                            ans += chr(j + ord('a')) * cnt[j]

                        return ans

            # Restore cnt for next iteration
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1

        return ""