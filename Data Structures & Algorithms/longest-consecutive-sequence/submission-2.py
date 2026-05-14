class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        output = 0
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                temp += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                if temp > output:
                    output = temp
                temp = 1
        
        if temp > output:
            output = temp

        return output