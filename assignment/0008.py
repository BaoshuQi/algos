class Solution:
    def myAtoi(self, str: str) -> int:
        s = set({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'})
        str = str.strip()
        ret = 0
        neg = False
        for i in range(0, len(str)):
            if i == 0 and str[0] == '-':
                neg = True
            elif i == 0 and str[0] == '+':
                neg = False
            elif str[i] in s:
                ret = ret * 10 + int(str[i])
            else:
                break

        limit = 1 << 31
        if neg:
            return -ret if ret < limit else -limit
        return ret if ret < limit - 1 else limit - 1

