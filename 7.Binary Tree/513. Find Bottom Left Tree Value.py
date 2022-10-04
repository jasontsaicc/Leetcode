# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = -1
        self.res = -1

    def left_value(self, root, left_depth):
        if root is None:
            return
        # 如果當前節點是葉子節點
        if root.left is None and root.right is None:
            # 當前葉子節點的深度大於之前保存的最大深度
            # 證明是當前深度的最左邊葉子節點，因為先遞迴左子樹
            # 此時更新最大深度，更新結果值

            if left_depth > self.max_depth:
                self.max_depth = left_depth
                self.res = root.val

        # 遞迴左子樹
        self.left_value(root.left, left_depth + 1)
        # 遞迴右子樹
        self.left_value(root.right, left_depth + 1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        self.left_value(root, 0)
        return self.res
