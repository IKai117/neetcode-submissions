class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.replace(' ', '').lower()
        print(a)
        if not a[-1].isalpha():
           a = a[:len(a)-1]
        if a == a[::-1]:
            return True
        else:
            return False