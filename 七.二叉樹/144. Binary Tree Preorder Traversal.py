# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def preorderTraversal(self, root):
#         result = []
#
#         def traversal(root):
#             if root is None:
#                 return
#             result.append(root.val)
#             traversal(root.left)
#             traversal(root.right)
#
#         traversal(root)
#         return result


# class Solution(TreeNode):
    def preorderTraversal(self, root):
        # 根結點為空則返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中結點先處理
            result.append(node.val)
            # 右孩子先入棧
            if node.right:
                stack.append(node.right)
            # 左孩子後入棧
            if node.left:
                stack.append(node.left)
        return result

s = TreeNode()
s.preorderTraversal([5, 4, 6, 1, 2])
