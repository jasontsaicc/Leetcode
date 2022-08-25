# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results

        #跟結點入queue
        queue = [root]
        while queue:
            results.append([node.val for node in queue])
            #存儲當前層的孩子節點列表
            result = []
            #對當前層的每個節點遍歷
            for node in queue:
                #如果左子節點存在，入隊列
                if node.left:
                    result.append(node.left)
                #如果右子節點存在，入隊列
                if node.right:
                    result.append(node.right)
            #後把queue更新成下一層的結點，繼續遍歷下一層
            queue = result
        return results
