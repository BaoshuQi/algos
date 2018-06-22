class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 1
        r = len(nums)
        mark = int((l + r ) / 2)
        while l != r:


            left = 0
            right = 0
            for n in nums:
                if n <= mark:
                    left += 1
                else:
                    right += 1
            if left >= mark + 1:
                r = mark
            else:
                l = mark + 1
            mark = int((l + r ) / 2)
        return mark


print(Solution.findDuplicate(Solution(), [1,2,3,4,4]))