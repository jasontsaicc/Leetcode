"""
Given a linked list, swap every two adjacent nodes and return its head. You
must solve the problem without modifying the values in the list's nodes (i.e., only
nodes themselves may be changed.)


 Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]


 Example 2:


Input: head = []
Output: []


 Example 3:


Input: head = [1]
Output: [1]



 Constraints:


 The number of nodes in the list is in the range [0, 100].
 0 <= Node.val <= 100


 Related Topics Linked List Recursion 👍 7524 👎 313

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        # 指針指向 虛擬頭結點
        cur = dummy_head

        # 如果是偶數的話cur.next 為空就結束 奇數的話 cur.next.next為空就結束
        while cur.next != None and cur.next.next != None:

            #  記錄臨時節點 這裡指向 1結點
            temp = cur.next
            # 這裡指向 3 結點
            temp1 = cur.next.next.next

            # 這裡開始步驟一 cur 指向 2
            cur.next = cur.next.next

            # 第二步 2指向1 但是這時候直接找1 以經找不到了 所以要用前面建立的temp指針 找到1
            # cur.next 是 2 2.next指向1
            cur.next.next = temp
            #第三步 1指向3
            temp.next = temp1

            # cur移動兩位，准備下一輪交換
            cur = cur.next.next

        # 這裡才是回傳第一結點
        return dummy_head.next
# leetcode submit region end(Prohibit modification and deletion)
