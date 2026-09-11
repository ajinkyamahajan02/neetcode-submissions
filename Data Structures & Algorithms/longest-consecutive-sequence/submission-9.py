class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        maxcons = 0
        
        for num in nums:
            if num-1 not in nums:
                current_cons = 1
            else:
                current_cons += 1
                maxcons = max(maxcons, current_cons)

        maxcons = max(maxcons, current_cons)
        return maxcons
        