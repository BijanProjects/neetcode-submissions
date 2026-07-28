class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {']':'[', ')':'(', '}':'{'}
        stack = []

        for i in s:
            if i not in hashmap:
                stack.append(i)
                continue
            if i in hashmap and not stack:
                return False
            if hashmap[i] != stack.pop():
                return False
        return not stack