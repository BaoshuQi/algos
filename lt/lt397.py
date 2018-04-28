# import Integer
class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        c = bin(int(n))[2:]
        while True:
            if c == '1':
                return count
            if c == '11':
                return count + 2
            if c[-1] == '0':
                c = c[:-1]
            elif c[-1] == c[-2] == '1':
                c = bin(int(c, 2) + 1)[2:]
            elif c[-1] == '1' and c [-2] == '0':
                c = bin(int(c, 2) - 1)[2:]
            count += 1

print(Solution.integerReplacement(Solution(), 3))