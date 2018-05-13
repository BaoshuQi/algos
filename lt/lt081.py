class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        if not nums:
            return False

        def fd(nums, left, right, target):
            if left == right and nums[left] != target:
                return False
            nmid = int((left + right) / 2)
            mid = nums[nmid]
            if mid == target:
                return True
            if nums[left] < nums[right]:
                if target > mid:
                    return fd(nums, nmid + 1, right, target)
                else:
                    return  fd(nums, left, nmid, target)
            elif nums[left] == nums[right]:
                return fd(nums, nmid + 1, right, target) or fd(nums, left, nmid, target)
            else:
                if mid >= target >= nums[left] or (nums[left] >= mid and target >= nums[left] >= nums[right]) or (nums[left] >= mid and target <= mid <= nums[right]):
                    return fd(nums, left, nmid, target)
                elif mid <= target <= nums[right] or (nums[right] <= mid and target >= nums[left] >= nums[right]) or (nums[right] <= mid and target <= nums[right]):
                    return fd(nums, nmid + 1, right, target)
                else:
                    return False

        return fd(nums, 0, len(nums) - 1, target)
