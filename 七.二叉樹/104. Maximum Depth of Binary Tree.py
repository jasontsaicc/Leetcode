# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 節點為空，高度為 0
        if not root:
            return 0

        # 遞迴計算左子樹的最大深度
        lefthight = self.maxDepth(root.left)
        # 遞迴計算右子樹的最大深度
        righthight  = self.maxDepth(root.right)
        # 二元樹的最大深度 = 子樹的最大深度 + 1（1 是根節點）
        return max(lefthight, righthight) + 1
