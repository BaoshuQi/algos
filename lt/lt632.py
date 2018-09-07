# not a good solution


class Solution:
    def find(self, m):
        upper = max(i[0] for i in m)
        lower = min(i[0] for i in m)
        rg = upper - lower
        rmn = min(len(i) for i in m)
        return upper, lower, rg, rmn

    def popmin(self, nums, n):
        index = []
        for l in range(0, len(nums)):
            if min(nums[l]) == n:
                nums[l] = [m for m in nums[l] if  m!= n]
                index.append(l)
        return nums, index

    def update(self, nums, m, index):
        # print(nums, m, index)
        for i in index:
            # print(m[i], nums[i])
            # minmum
            # if nums[i]
            m[i] = (min(nums[i]) if nums[i] else None, len(nums[i]))
        return m

    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        monitor = list()
        for n in nums:
            monitor.append((min(n), len(n)))

        f = self.find(nums)

        his = []

        while f[3] > 0:
            his.append(f)
            nums, index = self.popmin(nums, f[1])

            monitor = self.update(nums, monitor, index)
            for m in monitor:
                if m[1] == 0:
                    return list(self.smlrng(his))
            f = self.find(nums)

    def smlrng(self, his):
        m = min(h[2] for h in his)
        for h in his:
            if h[2] == m:
                return h[1],h[0]