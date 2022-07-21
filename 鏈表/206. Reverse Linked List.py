# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 雙指針
        #1.當前指針指向head, pre 指向none
        cur = head
        pre = None
        # 2.開始while循環 只要cur = None時就停止, 這時候pre會指向最後一位
        while cur != None:
            # 在建立一個臨時的指針 中間才不會斷掉
            # 保存一下 cur的下一個節點，因為接下來要改變cur->next
            temp = cur.next
            # 這裡就開始指針反轉了
            cur.next = pre
            # 更新pre、cur指針
            pre = cur
            # 如果沒有建立temp 這裡就找不到了
            cur = temp
        # 這時候的pre就是尾巴了, cur是指向None
        return pre