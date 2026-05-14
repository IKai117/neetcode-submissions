class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        slist.sort()
        tlist.sort()
        print(slist)
        print(tlist)
        if slist == tlist:
            return True
        return False
        