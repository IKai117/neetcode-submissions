class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res =  {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        
        count = list(res.values())
        count.sort()
        count.reverse()
        print(count)
        print(res)

        output = []
        for i in range(k):
            target = count[i]
            for m,x in res.items():
                if x == target:
                    if m in output:
                        continue
                    output.append(m)
            

        return output