class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                match c:
                    case ")":
                        begin = "("
                    case "]":
                        begin = "["
                    case "}":
                        begin = "{"
                    case _:
                        return False

                if len(stack) > 0 and stack[-1] == begin:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
