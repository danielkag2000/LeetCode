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
        n = self.get_len(head)
        if n <= 1:
            return None
        mid = n / 2
        s = head
        for i in range(1, mid):
            s = s.next
        m = s.next
        e = m.next
        m.next = None
        s.next = e
        return head
        
    def get_len(self, head):
        n = 0
        while head is not None:
            head = head.next
            n += 1
        return n