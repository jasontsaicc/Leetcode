# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 如果要刪除的是 N 的結點 指針要指向 N的上一個
        # 也是使用dummy head 就不用擔心要刪第一個結點
        # 設定快, 慢指針在 dummy head
        # 先移動 fast 移動N步 在一起移動 slow, fast 直到 fast指到None
        # 問題一, 一定要有指針在N的前一個
        #  fast 走N+1 步 例如 n = 2 fast 走到 3
        # 快慢在同時移動 直到fast 走到 None , slow 也會剛好走到 N的 上一個
        # 讓slow的next 指向 next.next

        # 添加一個虛擬節點
        dummy_head = ListNode(next=head)
        slow = dummy_head
        fast = dummy_head

        for _ in range(n):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

            # 此時fast.next為空，說明fast是尾結點
            # slow.next為倒數第n個節點
            # 下面進行刪除倒數第n個節點的操作
            slow.next = slow.next.next
        return dummy_head.next
