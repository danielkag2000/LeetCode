# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        elements = set()
        
        # go over the tree
        queue = [root]
        while queue:
            l = queue.pop(0)
            
            if k - l.val in elements:
                return True
            else:
                elements.add(l.val)
            
            if l.left is not None:
                queue.append(l.left)
            if l.right is not None:
                queue.append(l.right)
        
        return False
        