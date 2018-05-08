class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        import collections
        counter = collections.Counter(nums)
        s = list(set(nums))
        s.sort()
        max = 0
        n1 = s[0]
        for n in s:
            if n - n1 == 1 and counter[n1] + counter[n] > max:
                max = counter[n1] + counter[n]
            n1 = n
        return max


