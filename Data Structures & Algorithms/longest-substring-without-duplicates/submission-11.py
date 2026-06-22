class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        res = 0
        for i in range(len(s)):
            if s[i] in substring:
                res = max(res, len(substring))
                j=0
                while True:
                    j-=1
                    if substring[j] == s[i]:
                        index = len(substring) + j
                        break
                temp = substring.copy()
                substring.clear()
                for k in range(index+1, len(temp)):
                    substring.append(temp[k])
                substring.append(s[i])
                
            else:
                substring.append(s[i])
            print(substring)
            
        res = max(res, len(substring))
        return res