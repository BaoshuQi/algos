class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.l = [0]

        for i in range(0, len(nums)):
            self.l.append(self.l[-1] + nums[i])
        print(self.l)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.l[j + 1] - self.l[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
