# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 初始化 res
    def __init__(self):
        self.res = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        # 2.確定終止條件
        # 遞迴中止條件
        if root is None:
            return 0

        # 3.確定單層遞迴的邏輯(找出重複的子問題)
        # 如果遍歷到當前節點的左孩子為左葉節點，則將左孩子的值加入 res
        if root.left != None and root.left.left == None and root.left.right == None:
            self.res += root.left.val
        # 遍歷左子樹
        self.sumOfLeftLeaves(root.left)
        # 遍歷右子樹
        self.sumOfLeftLeaves(root.right)
        return self.res