from collections import deque


class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        """
           1. 首先確認不空
           2. 因為隊列的特殊性，FIFO，所以我們只有在pop()的時候才會使用queue_out
           3. 先把queue_in中的所有元素（除了最後一個），依次出列放進queue_out
           4. 交換in和out，此時out裡只有一個元素
           5. 把out中的pop出來，即是原隊列的最後一個

           tip：這不能像棧實現隊列一樣，因為另一個queue也是FIFO，如果執行pop()它不能像
           stack一樣從另一個pop()，所以乾脆in只用來存數據，pop()的時候兩個進行交換
           """
        # 1. 首先確認不空
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            # 3. 先把queue_in中的所有元素（除了最後一個），依次出列放進queue_out
            self.queue_out.append(self.queue_in.popleft())
        # 4.交換in和out，此時out裡只有一個元素
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        # 5.把out中的pop出來，即是原隊列的最後一個
        return self.queue_out.popleft()

    def top(self) -> int:
        """
              1. 首先確認不空
              2. 我們僅有in會存放數據，所以返回第一個即可
        """
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self) -> bool:
        """
        因為只有in存了數據，只要判斷in是不是有數即可
        """
        return len(self.queue_in) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
