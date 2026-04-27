class Solution:
    def findMin(self, nums: List[int]) -> int:
        head = 0
        tail = len(nums) - 1

        while head < tail:
            mid = (head + tail) // 2

            if nums[mid] > nums[tail]:
                head = mid + 1
            else:
                tail = mid
        return nums[head]        