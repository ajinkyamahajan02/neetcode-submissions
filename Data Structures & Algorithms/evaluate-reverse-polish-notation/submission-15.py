class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            try:
                token = float(token)
                stk.append(token)
            except:
                element2 = stk.pop()
                element1 = stk.pop()
                res = eval(str(element1) + str(token) + str(element2))
                stk.append(res)

        return int(stk[-1])
            