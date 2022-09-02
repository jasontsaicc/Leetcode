class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(item)
            else:
                first_num, second_num = stack.pop(), stack.pop()
                # 第一個出來的在運算符後面
                stack.append(
                    int(eval(f'{second_num}{item}{first_num}')))

                # 如果一開始只有一個數，那麼會是字符串形式的
        return int(stack.pop())