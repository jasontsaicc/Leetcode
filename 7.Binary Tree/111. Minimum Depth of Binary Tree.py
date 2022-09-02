# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 1.確定終止條件re
        if root == None:
            return 0

        # 2.找出重複的子問題
        # 1.只有根節點，最小高度為 1
        if root.left == None and root.right == None:
            return 1

        # 左子樹最小值和右子樹最小值
        leftMinDepth = self.minDepth(root.left)
        rightMinDepth = self.minDepth(root.right)

        # 2.如果節點的左子樹不為空，右子樹為空
        if root.left != None and root.right == None:
            return leftMinDepth + 1
        # 3.如果節點的右子樹不為空，左子樹為空
        if root.right != None and root.left == None:
            return rightMinDepth + 1
        # 4.左右子樹都不為空
        return min(leftMinDepth, rightMinDepth) + 1

