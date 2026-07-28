class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''

        for i in range(len(strs)):
            output += str(len(strs[i])) + '#' + strs[i]

        return output

        

    def decode(self, s: str) -> List[str]:
        output = []
        start = 0

        for i in range(len(s)):
            if i < start:
                continue
            if s[i] == '#':
                num = int(s[start:i])
                output.append(s[i+1:i+1+num])
                start = i+1+num
        return output