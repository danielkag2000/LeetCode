# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # get len
        n = 0
        s = head
        while s is not None:
            s = s.next
            n += 1
        
        if n <= 1:
            return None
        
        # remove mid
        s = head
        for i in range(1, n / 2):
            s = s.next
        m = s.next
        e = m.next
        m.next = None
        s.next = e
        return head
