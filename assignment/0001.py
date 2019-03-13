class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()
        for i in range(0, len(nums)):
            if nums[i] in d and nums[i] * 2 == target:
                return [i, d[nums[i]][0]]
            d[nums[i]] = (i, target - nums[i])

        for i in d.keys():
            if d[i][1] in d and d[i][1] != d[d[i][1]][1]:
                return [d[i][0], d[d[i][1]][0]]