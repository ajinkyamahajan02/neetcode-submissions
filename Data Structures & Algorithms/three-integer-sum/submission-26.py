class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        start = 0
        curr = start + 1
        end = len(nums)-1

        for start in range(len(nums)-2):
            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
                curr = start + 1
                continue

            while curr < end:

                s = nums[start] + nums[curr] + nums[end] 
                if s == 0:
                    res.append([nums[start],nums[curr],nums[end]])
                    curr += 1
                    end -= 1

                if s < 0:
                    curr += 1

                if s > 0:
                     end -= 1

            start += 1
            curr = start + 1
            end = len(nums)- 1
        return res             

        