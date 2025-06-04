from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert a positive integer (num) into its Roman‐numeral representation.
        We’ll reuse your `roman_lookup` for the seven “base” symbols:
            1 → "I", 5 → "V", 10 → "X", 50 → "L", 100 → "C", 500 → "D", 1000 → "M".

        Then we’ll build the “subtractive cases” (4, 9, 40, 90, 400, 900) by
        concatenating two base‐symbols appropriately:
            4  = "IV"  (= I + V)
            9  = "IX"  (= I + X)
            40 = "XL"  (= X + L)
            90 = "XC"  (= X + C)
            400 = "CD" (= C + D)
            900 = "CM" (= C + M)

        Finally, we perform a simple “greedy” pass: iterate from largest value → smallest,
        repeatedly subtracting that value from `num` and appending its symbol until `num == 0`.
        """

        # ------------------------------------------------------------
        # 1) Build your original `roman_lookup` for the 7 base values
        # ------------------------------------------------------------
        roman_lookup: Dict[int, str] = defaultdict(str)
        roman_lookup[1] = "I"
        roman_lookup[5] = "V"
        roman_lookup[10] = "X"
        roman_lookup[50] = "L"
        roman_lookup[100] = "C"
        roman_lookup[500] = "D"
        roman_lookup[1000] = "M"

        # We will create a list of (value, symbol) pairs in descending order:
        value_symbol_pairs: List[Tuple[int, str]] = [
            (1000, roman_lookup[1000]),  # "M"
            (900, roman_lookup[100] + roman_lookup[1000]),  # "CM"
            (500, roman_lookup[500]),  # "D"
            (400, roman_lookup[100] + roman_lookup[500]),  # "CD"
            (100, roman_lookup[100]),  # "C"
            (90, roman_lookup[10] + roman_lookup[100]),  # "XC"
            (50, roman_lookup[50]),  # "L"
            (40, roman_lookup[10] + roman_lookup[50]),  # "XL"
            (10, roman_lookup[10]),  # "X"
            (9, roman_lookup[1] + roman_lookup[10]),  # "IX"
            (5, roman_lookup[5]),  # "V"
            (4, roman_lookup[1] + roman_lookup[5]),  # "IV"
            (1, roman_lookup[1]),  # "I"
        ]

        # ------------------------------------------------------------
        # 3) Now run a simple “greedy” loop from largest → smallest
        # ------------------------------------------------------------
        res: List[str] = []
        remaining = num


        for value, symbol in value_symbol_pairs:
            if remaining == 0:
                break

            # How many times does `value` fit into `remaining`?
            count = remaining // value
            if count > 0:
                # Append that symbol `count` times
                res.append(symbol * count)
                # Subtract off from remaining
                remaining -= value * count

        # Join all pieces together into one final Roman string
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    for x in [3, 4, 9, 58, 1994, 3749]:
        print(x, "→", s.intToRoman(x))
