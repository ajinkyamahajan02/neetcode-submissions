class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for element in s:
            if element in (['(', '{', '[']):
                stk.append(element)

            if element == '}':
                if stk[-1] == '{':
                    stk.pop()
                else:
                    return False

            if element == ']':
                if stk[-1] == '[':
                    stk.pop()
                else:
                    return False

            
            if element == ')':
                if stk[-1] == '(':
                    stk.pop()
                else:
                    return False

        if stk:
            return False

        return True
        