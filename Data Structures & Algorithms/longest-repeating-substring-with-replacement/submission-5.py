class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        temp = k
        res = 0
        last = False
        for i in s:
            if temp == 0:
                last = True 
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
            
            res = max(res, r)

        return res