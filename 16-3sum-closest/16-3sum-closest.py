import itertools

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """       
        l = len(nums)
        nums.sort()
        min_sum = min_diff = 100000
        
        for i in range(l):
            j = i + 1
            k = l - 1
            while j < k:
                p_sum = nums[i] + nums[j] + nums[k]
                diff = abs(p_sum - target)
                
                if diff < min_diff:
                    min_diff = diff
                    min_sum = p_sum
                
                if p_sum > target:
                    k -= 1
                else:
                    j += 1
                
        return min_sum