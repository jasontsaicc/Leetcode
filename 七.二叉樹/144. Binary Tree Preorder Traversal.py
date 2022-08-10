# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root):
        result = []

        def traversal(root):
            if root is None:
                return
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return result


s = Solution()
s.preorderTraversal(root=[1, 2, 3])
