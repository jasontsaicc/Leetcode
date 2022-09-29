# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1.遞迴函數函數參數以及返回值
    def get_paths(self, root, path, res):
        if not root:
            return
        # 結點值加入當前路徑
        path += str(root.val)

        # 2.確定遞歸的終止條件
        # 如果當前節點是葉子節點, 將當前路徑加到res
        if root.left is None and root.right is None:
            res.append(path)

        # 3.找出重複的子問題
        else:
            path += '->'
            self.get_paths(root.left, path, res)
            self.get_paths(root.right, path, res)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.get_paths(root, '', res)

        return res
