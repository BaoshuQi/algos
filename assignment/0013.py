class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        last = ' '
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, ' ': 0}
        for c in reversed(s):
            if d[last] <= d[c]:
                ret += d[c]
            else:
                ret -= d[c]
            last = c

        return ret
