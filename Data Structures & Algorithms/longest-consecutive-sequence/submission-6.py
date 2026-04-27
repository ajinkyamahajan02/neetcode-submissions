class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = {}

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        for num in nums:
            if num-1 not in set(nums):
                temp_lst = 1
                while(num+1 in nums):
                    temp_lst += 1
                    num = num+1
                lookup[num] = temp_lst

        return max(lookup.values())

        