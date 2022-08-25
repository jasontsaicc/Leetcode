# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 1.設立終止條件
        ans = []
        if not root:
            return ans
        # 2.根結點入quere(隊列)
        que = [root]
        while que:
        # 3.把當層que結點的值入隊列
            ans.append([node.val for node in que][-1])
        # 4.遍歷當前層queue的每個結點的左子結點，右子結點，入隊列
            result = []
            for node in que:
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
            que = result
        return ans

        # 5.最後返回results