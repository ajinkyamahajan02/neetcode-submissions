class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token in ['+', '-', '/', '*']:
                element2 = stk.pop()
                element1 = stk.pop()

                if token == '+':
                    stk.append(element1 + element2)
                elif token == '-':
                    stk.append(element1 - element2)
                elif token == '/':
                    stk.append(int(element1 / element2))
                elif token == '*':
                    stk.append(element1 * element2)

            else:
                stk.append(int(token))

        return int(stk[0])