class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # mark = True
        tag = 0
        for i in range(0, len(A) - 1):
            if A[i + 1] - A[i] == 0:
                continue
            elif A[i + 1] - A[i] < 0:
                mark = -1
            else:
                mark = 1
            if mark * tag < 0:
                return False
            tag = mark
        return True


s = Solution()

print(s.isMonotonic([1,2,2,3]))
print(s.isMonotonic([6,5,4,4]))
print(s.isMonotonic([1,3,2]))
print(s.isMonotonic([1,2,4,5]))
print(s.isMonotonic([1,1,1]))

