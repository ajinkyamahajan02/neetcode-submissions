class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                top = stack.pop()
                second_top = stack.pop()

                if token == "+":
                    stack.append(int(second_top + top))
                elif token == "-":
                    stack.append(int(second_top - top))
                elif token == "*":
                    stack.append(int(second_top * top))
                elif token == "/":
                    stack.append(int(second_top / top))
                
            else:
                stack.append(int(token))

        return stack[0]