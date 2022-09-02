# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
#
#
#  Example 1:
#
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
#
#  Example 2:
#
#
# Input: head = [], val = 1
# Output: []
#
#
#  Example 3:
#
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 10⁴].
#  1 <= Node.val <= 50
#  0 <= val <= 50
#
#
#  Related Topics Linked List Recursion 👍 5418 👎 172


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 這裡採用添加虛擬節點的方式
        # 將虛擬頭結點指向head，這樣方面後面做刪除操作
        dummy_head = ListNode(next=head)
        #當前結點= 剛建立的虛擬結點
        cur = dummy_head
        # 只要還有下一個不為空 就繼續執行
        while(cur.next!=None):

            # 如果找到需要刪除的結點
            if(cur.next.val == val):
                # 刪除cur.next節點 就是把指針指向下個節點next的next
                cur.next = cur.next.next
            else:
                cur = cur.next
        # 注意返回的要是dummy_head虛擬結點的下一個
        return dummy_head.next


# leetcode submit region end(Prohibit modification and deletion)
