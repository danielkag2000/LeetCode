class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        nums.sort()
        tripels = []
        d = set()
        
        for i in range(l):
            j = i + 1
            k = l - 1
            while j < k:
                p_sum = nums[i] + nums[j] + nums[k]
                if p_sum == 0:
                    s = '{0},{1},{2}'.format(nums[i],nums[j],nums[k])
                    if s not in d:
                        tripels.append([nums[i], nums[j], nums[k]])
                        d.add(s)
                
                if p_sum > 0:
                    k -= 1
                else:
                    j += 1
                
        return tripels