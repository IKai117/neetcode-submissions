class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        temp = k
        res = 0
        last = False
        for i in s:
            if i == s[l]:
                r += 1
            elif last:
                temp = k
                last = False
                l = s.index(i) + 1
                r = 0
                continue
            else:
                temp -= 1
                r += 1
            if temp == 0:
                last = True 
            res = max(res, r)

        return res