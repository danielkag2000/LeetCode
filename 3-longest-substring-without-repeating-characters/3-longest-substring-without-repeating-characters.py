class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        for i in range(n):
            d = set()
            for j in range(i, n):
                if s[j] in d:
                    break
                d.add(s[j])
            count = len(d) if count < len(d) else count
        return count