# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 如果樹為空，返回 False
        if root is None:
            return False
        # 如果當前節點為葉子節點，且葉子節點的值等於減去該路徑之前節點的值，返回 True
        if root.left is None and root.right is None and root.val == targetSum:
            return True
        # 遞迴左子樹
        left_path = self.hasPathSum(root.left, targetSum - root.val)
        # 遞迴右子樹
        right_path = self.hasPathSum(root.right, targetSum - root.val)

        return left_path or right_path