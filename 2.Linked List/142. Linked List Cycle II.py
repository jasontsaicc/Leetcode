# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 使用快慢指針, 只要有環 快慢就一定可以相遇
        # fast 每次移動 2 slow 每次移動 1 fast, 相對於 slow 每次 +1
        # 如何找到環的入口
        # 開始到環的入口 設X, 入口到相遇 Y, 相遇到入口 Z
        # slow = x + y  每次走1
        # fast = x + y + n(y + z) 每次走2
        # 2(x+y) = x + y + n(y + z)
        # x + y = n(y + z)
        # x = n(y + z) - y