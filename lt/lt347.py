class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dict = {}
        rev = {}
        for n in nums:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
        for ke in dict:
            if dict[ke] in rev:
                rev[dict[ke]].append(ke)
            else:
                rev[dict[ke]] = [ke]
        keys = sorted(rev.keys())[::-1]
        ret = []
        i = 0
        while len(ret) < k:
            ret += rev[keys[i]]
            i += 1
        return ret

print(Solution.topKFrequent(Solution(), [1,2], 2))
