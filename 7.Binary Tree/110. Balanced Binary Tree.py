# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 1. 明確遞歸函數的參數和返回值
        if self.get_height(root) != -1:
            return True
        else:
            return False

    def get_height(self, root):

        # 2.明確的終止條件
        if not root:
            return 0

        # 3.明確單層遞歸的邏輯(後序遍歷的順序為左右中)
        # 左
        if (left_height := self.get_height(root.left)) == -1:
            return -1
            # 右
        if (right_height := self.get_height(root.right)) == -1:
            return -1
            # 中
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)
