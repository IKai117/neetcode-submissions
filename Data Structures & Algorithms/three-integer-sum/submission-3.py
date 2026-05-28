class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(1, len(nums)-1):
            chase = -nums[i]
            x = 0
            y = len(nums)-1
            while x < y:
                if nums[x] + nums[y] > chase:
                    while True:
                        y -= 1
                        if y != i:
                            break
                elif nums[x] + nums[y] < chase:
                    while True:
                        x += 1
                        if x != i:
                            break
                elif nums[x] + nums[y] == chase:
                    ans = sorted([nums[i], nums[x], nums[y]])
                    if ans not in res:
                       res.append(ans)
                    while True:
                        x += 1
                        if x != i:
                            break
                    while True:
                        y -= 1
                        if y != i:
                            break
        return res