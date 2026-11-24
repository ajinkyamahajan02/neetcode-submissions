class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, curr, totalSum):
            if totalSum == target:
                res.append(curr.copy())
                return 
            
            if index >= len(nums) or totalSum > target:
                return 
            
            curr.append(nums[index])
            dfs(index, curr, totalSum+nums[index])

            curr.pop()
            dfs(index+1, curr, totalSum)

        dfs(0, [], 0)
        return res