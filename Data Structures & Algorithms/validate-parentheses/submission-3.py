class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'}':'{', ']':'[', ')':'('}

        for i in s:
            if i in hashmap:
                
                if not stack:
                    return False
                
                if stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True