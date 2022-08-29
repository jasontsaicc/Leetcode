# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 遞迴終止條件
        if root == None:
            return None
        # 將當前節點的左右子樹交換
        root.left, root.right = root.right, root.left
        # 遞迴左子樹
        self.invertTree(root.left)
        # 遞迴右子樹
        self.invertTree(root.right)
        return root

