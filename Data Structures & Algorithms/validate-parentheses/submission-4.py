class Solution:
    def isValid(self, s: str) -> bool:
        baseMap = {")": "(", "]" : "[", "}": "{"}
        stack = []

        for c in s:
            if c in baseMap:
                if stack and stack[-1] == baseMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
                