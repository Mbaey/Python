class Solution:
    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    def romanToInt(self, s: str) -> int:
        res = 0
        for value, symbol in Solution.VALUE_SYMBOLS:
            while s.startswith(symbol):
                res += value
                s = s[len(symbol):]
                # num -= value
                # roman.append(symbol)
            if s == "":
                break
        return res