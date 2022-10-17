class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s = set()
        for a in sentence:
            s.add(a)
            
        return len(s) == 26