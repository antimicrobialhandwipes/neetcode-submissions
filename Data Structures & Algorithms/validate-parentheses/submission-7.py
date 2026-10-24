class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_to_open = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in closed_to_open.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != closed_to_open[char]:
                    return False

        return len(stack) == 0