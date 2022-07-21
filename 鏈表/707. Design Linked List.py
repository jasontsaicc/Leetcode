# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list. A node in a singly linked list should have two
# attributes: val and next. val is the value of the current node, and next is a pointer/
# reference to the next node. If you want to use the doubly linked list, you will
# need one more attribute prev to indicate the previous node in the linked list.
# Assume all nodes in the linked list are 0-indexed.
#
#  Implement the MyLinkedList class:
#
#
#  MyLinkedList() Initializes the MyLinkedList object.
#  int get(int index) Get the value of the indexᵗʰ node in the linked list. If
# the index is invalid, return -1.
#  void addAtHead(int val) Add a node of value val before the first element of
# the linked list. After the insertion, the new node will be the first node of the
# linked list.
#  void addAtTail(int val) Append a node of value val as the last element of
# the linked list.
#  void addAtIndex(int index, int val) Add a node of value val before the indexᵗ
# ʰ node in the linked list. If index equals the length of the linked list, the
# node will be appended to the end of the linked list. If index is greater than the
# length, the node will not be inserted.
#  void deleteAtIndex(int index) Delete the indexᵗʰ node in the linked list, if
# the index is valid.
#
#
#
#  Example 1:
#
#
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
#
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
#
#
#
#  Constraints:
#
#
#  0 <= index, val <= 1000
#  Please do not use the built-in LinkedList library.
#  At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and
# deleteAtIndex.
#
#
#  Related Topics Linked List Design 👍 1640 👎 1246


# leetcode submit region begin(Prohibit modification and deletion)

# 這裡我使用單鏈表
# 先定義鏈表節點結構體
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    # 初始化鏈表
    def __init__(self):
        self._dummyHead = Node(0)  # 虛擬頭部節點
        self._count = 0  # 添加的節點數

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        # 獲取到第index個節點數值，如果index是非法數值直接返回 - 1， 注意index是從0開始的，第0個節點就是頭結點
        if 0 <= index < self._count:
            node = self._dummyHead

            for _ in range(index + 1):
                # 從1開始 沒獲取到就繼續往下找
                node = node.next
            # 找到了 就回傳
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # 這裡直接使用_count 計數來加入就可以了
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # 這裡直接使用_count 計數來加入就可以了
        self.addAtIndex(self._count, val)

    # 在第index個節點之前插入一個新節點，例如index為0，那麼新插入的節點為鏈表的新頭節點。
    # 如果index 等於鏈表的長度，則說明是新插入的節點為鏈表的尾結點
    # 如果index大於鏈表的長度，則返回空

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return

        # 計數累加
        self._count += 1

        add_node = Node(val)
        prev_node, current_node = None, self._dummyHead
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._count:
            # 計數-1
            self._count -= 1
            prev_node, current_node = None, self._dummyHead
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node.next, None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# leetcode submit region end(Prohibit modification and deletion)
