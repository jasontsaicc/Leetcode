# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        # 1.確定終止條件 如果當前遍歷的這個節點是空，就直接return
        if not root:
            return ans
        que = [root]
        while que:
            # 存儲當前層的孩子節點列表
            ans.append([node.val for node in que])
            res = []
            # 對當前層的每個節點遍歷
            for node in que:
                # 如果左子節點存在，入隊列
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            # #後把queue更新成下一層的結點，繼續遍歷下一層
            que = res
        # 列表倒序
        return ans[::-1]