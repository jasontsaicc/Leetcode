# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1.定義函數求二元樹的深度
    def height(self, root):
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def countNodes(self, root: TreeNode) -> int:
        # 2.空樹, 結點為0
        if root is None:
            return 0
        # 3.求左子樹和右子樹的深度
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        # 如果左子樹的深度 = 右子樹的深度，左子樹為滿二元樹
        # 節點數 = 左子樹的深度 + 右子樹的深度 + 根節點
        if leftHeight == rightHeight:
            return (2 ** rightHeight - 1)  + self.countNodes(root.right) + 1
        else:
            return (2 ** rightHeight - 1) + self.countNodes(root.left) + 1

