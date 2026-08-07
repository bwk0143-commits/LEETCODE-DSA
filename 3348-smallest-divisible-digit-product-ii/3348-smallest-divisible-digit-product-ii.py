class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Prime-factor contributions of digits 0..9: (2, 3, 5, 7)
        digit_factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        # Factorize t using primes possible in a digit product.
        need = [0, 0, 0, 0]
        for index, prime in enumerate((2, 3, 5, 7)):
            while t % prime == 0:
                need[index] += 1
                t //= prime

        # A digit product can never contain primes greater than 7.
        if t != 1:
            return "-1"

        def remaining(required, used):
            return [max(0, required[i] - used[i]) for i in range(4)]

        def smallest_suffix(req):
            """
            Return the shortest, lexicographically smallest digit string
            whose digit product contains all factors in req.
            """
            twos, threes, fives, sevens = req
            result = []

            # Use 8 and 9 to minimize digit count.
            result.extend("8" * (twos // 3))
            twos %= 3

            result.extend("9" * (threes // 2))
            threes %= 2

            # Resolve remaining powers of 2 and 3.
            if twos == 1 and threes == 1:
                result.append("6")
            elif twos == 2 and threes == 1:
                result.extend(["2", "6"])
            else:
                if twos == 2:
                    result.append("4")
                elif twos == 1:
                    result.append("2")

                if threes == 1:
                    result.append("3")

            result.extend("5" * fives)
            result.extend("7" * sevens)

            return "".join(sorted(result))

        n = len(num)

        # Find the first zero. A valid answer cannot preserve a zero.
        first_zero = num.find("0")

        # If num has no zero, check whether it already satisfies the condition.
        if first_zero == -1:
            current_factors = [0, 0, 0, 0]

            for ch in num:
                factors = digit_factors[ord(ch) - ord("0")]
                for i in range(4):
                    current_factors[i] += factors[i]

            if remaining(need, current_factors) == [0, 0, 0, 0]:
                return num

            # We can initially try changing the final digit.
            start_pos = n - 1
        else:
            # We must change this zero or an earlier digit.
            start_pos = first_zero

        # Factor contributions from num[0:start_pos].
        prefix = [0, 0, 0, 0]
        for i in range(start_pos):
            factors = digit_factors[ord(num[i]) - ord("0")]
            for j in range(4):
                prefix[j] += factors[j]

        # Try changing the rightmost possible digit first.
        for pos in range(start_pos, -1, -1):
            current_digit = ord(num[pos]) - ord("0")
            suffix_slots = n - pos - 1

            # Make num[pos] larger by the smallest possible amount.
            for new_digit in range(current_digit + 1, 10):
                used = prefix[:]
                factors = digit_factors[new_digit]

                for j in range(4):
                    used[j] += factors[j]

                suffix = smallest_suffix(remaining(need, used))

                if len(suffix) <= suffix_slots:
                    # Leading 1s make the suffix lexicographically smallest.
                    return (
                        num[:pos]
                        + str(new_digit)
                        + "1" * (suffix_slots - len(suffix))
                        + suffix
                    )

            # Shift the changed position one step left.
            if pos > 0:
                factors = digit_factors[ord(num[pos - 1]) - ord("0")]
                for j in range(4):
                    prefix[j] -= factors[j]

        # No valid same-length number exists.
        # Any longer number is greater than num.
        core = smallest_suffix(need)
        answer_length = max(n + 1, len(core))

        return "1" * (answer_length - len(core)) + core