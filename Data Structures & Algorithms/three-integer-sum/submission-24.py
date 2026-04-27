class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        head = 0
        curr = 0
        res_lst = []
        nums.sort()

        while head < len(nums)-2:

            if head > 0 and nums[head] == nums[head-1]:
                head += 1
                continue
                
            curr = head + 1
            tail = len(nums)-1

            while curr < tail:
                total = nums[head] + nums[curr] + nums[tail]

                if total == 0:
                    res_lst.append([nums[head], nums[curr], nums[tail]])
                    while curr < tail and nums[curr] == nums[curr + 1]:
                        curr += 1
                    while curr < tail and nums[tail] == nums[tail - 1]:
                        tail -= 1

                    curr += 1
                    tail -= 1
                
                elif total > 0:
                    tail -= 1
                else:
                    curr += 1

            head += 1

        return res_lst
        