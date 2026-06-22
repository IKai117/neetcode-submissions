class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        res = 0
        temp = 0
        for i in range(len(s)):
            if s[i] in substring:
                res = max(res, len(substring))
                substring = [s[i]]
                
            else:
                substring.append(s[i])
                temp = len(substring)
            
        res = max(res, temp)
        return res