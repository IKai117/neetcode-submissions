class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count = {}
        res_count = []
        res = ""

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
                        if count.get(s[l], 0) == 1:
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
            if len(list(count.keys())) == len(t):
                # while l < r:                                     
                        # if count[s[l]] == 1:
                        #     break
                        # elif s[l] in count:
                        #     count[s[l]] -= 1
                        # res = res[1:]
                        # l+=1
                res_count.append(res)

            print(count.keys() )
            print(res)

        if res_count:
            res_count = sorted(res_count, key = lambda x: len(x))
            print(res_count)
            return res_count[0]
        else:
            return ""

        