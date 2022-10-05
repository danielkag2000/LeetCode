class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,x in enumerate(nums):
            if target - x in d:
                return [i, d[target-x]]
            d[x] = i
        return []
                