class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = [0] * (target+1)
        
        n[0] = 1
        for i in range(target+1):
            for j in nums:
                if i + j < target + 1:
                    n[i + j] += n[i]
        return n[-1]           
        