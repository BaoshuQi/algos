class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        c = 1
        for n in range (2, int(num ** 0.5) + 1):
            if num % n == 0:
                c += n + num/n
            if c > num:
                return False
        if c == num:
            return True
        return False


print(Solution.checkPerfectNumber(Solution(), 6))