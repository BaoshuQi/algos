class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ret = -int(str(-x)[::-1])
        else:
            ret = int(str(x)[::-1])
        t = 2 ** 31
        if ret >= - t and ret <= t - 1:
            return ret
        else:
            return 0