class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        s = A
        max =len(B) / len(A) + 2 if len(B) > len(A) else 3
        count = 1
        while B not in A:
            count += 1
            A += s
            if max < count:
                return -1
        return count
