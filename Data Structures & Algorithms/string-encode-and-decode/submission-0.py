class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += i
            s += ';'
        return s
    def decode(self, s: str) -> List[str]:
        outcome = []
        index = 0
        outcome.append("")
        for i in s:
            if i != ';':
                outcome[index] += i
            else:
                outcome.append("")
                index += 1
        outcome.pop()
        return outcome

