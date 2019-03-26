class Solution:
    def intToRoman(self, num: int) -> str:
        ch = ['M', 'CM', 'D', 'CD', 'C',
              'XC', 'L', 'XL', 'X',
              'IX', 'V', 'IV', 'I']
        val = [1000, 900, 500, 400, 100,
               90, 50, 40, 10,
               9, 5, 4, 1]
        ret = ''
        for i in range(len(val)):
            n = num // val[i]

            if n != 0:
                ret += ch[i] * n
                num -= val[i] * n

        return ret
    