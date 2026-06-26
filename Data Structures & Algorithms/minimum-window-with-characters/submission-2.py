class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count = {}
        res_count = []
        res = ""
        t_count = {}
        for i in range(len(t)):
            if t[i] in t_count:
                t_count[t[i]] += 1
            else:
                t_count[t[i]] = 1
        print(t_count)

        for r in range(len(s)):
            # res 裡面已經有東西
            if res and s[r] not in t: #字元不在t
                res += s[r]
            elif res and s[r] in t: #字元在t
                if count.get(s[r], 0) == 0: #字元第一次出現
                    res += s[r]
                    count[s[r]] = 1
                else: #字元第二次出現
                    res += s[r]
                    count[s[r]] += 1
                    # l 增加 並檢查
                    while l < r:
                        print("in")
                        if s[l] in t and count[s[l]] == t.count(s[l]):
                            break
                        elif s[l] in count:
                            count[s[l]] -= 1
                        l+=1
                        res = res[1:]
                    
            # res 裡面沒東西
            if s[r] in t and count.get(s[r], 0) == 0:
                l = r
                res += s[r]
                count[s[r]] = 1

            #判斷res是否合格
            # if len(list(count.keys())) == len(t): #方法一
            #     res_count.append(res)
            valid = True
            for i in t:

                if res.count(i) < t_count[i]:
                    valid = False
            if valid:
                res_count.append(res)

            print(count.keys() )
            print(res)

        if res_count:
            res_count = sorted(res_count, key = lambda x: len(x))
            print(res_count)
            return res_count[0]
        else:
            return ""

        