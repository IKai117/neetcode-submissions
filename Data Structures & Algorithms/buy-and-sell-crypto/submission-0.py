class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in prices:
            for j in prices[prices.index(i)+1:]:
                print(j-i)
                if j - i > res:
                    res = j-i
        return res
