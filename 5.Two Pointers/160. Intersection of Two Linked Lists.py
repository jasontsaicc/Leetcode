class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        根據快慢法則，走的快的一定會追上走得慢的。
        在這道題裡，有的鏈表短，他走完了就去走另一條鏈表，我們可以理解為走的快的指針。

        那麼，只要其中一個鏈表走完了，就去走另一條鏈表的路。如果有交點，他們最終一定會在同一個
        位置相遇
        """
        if headA is None or headB is None:
            return None
        # 用兩個指針代替a和b
        cur_a, cur_b = headA, headB

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB
            cur_b = cur_b.next if cur_b else headA

        return cur_a

