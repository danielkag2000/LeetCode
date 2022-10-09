class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        template = '{} ' * len(nums)
        p_permutations = list(permutations(nums))
        d = set()
        res = []
        for p in p_permutations:
            s = template.format(*p)
            if s not in d:
                d.add(s)
                res.append(p)
        
        return res