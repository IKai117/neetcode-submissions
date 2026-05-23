class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.replace(' ', '').lower()
        
        for i in a:
            # print(i)
            if not i.isalpha():
                a = a.replace(i, '')
        # if not a[-1].isalpha():
        #    a = a[:len(a)-1]
        print(a)
        if a == a[::-1]:
            return True
        else:
            return False