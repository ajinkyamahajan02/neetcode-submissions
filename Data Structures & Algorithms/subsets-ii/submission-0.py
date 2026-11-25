class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(index, curr):
            if index >= len(nums):
                res.append(curr.copy())
                return 
            
            curr.append(nums[index])
            dfs(index+1, curr)

            curr.pop()
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            
            dfs(index+1, curr)

        dfs(0, [])
        return res