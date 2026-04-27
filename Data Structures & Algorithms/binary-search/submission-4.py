class Solution:
    def search(self, nums: List[int], target: int) -> int:
        tail = len(nums)-1
        head = 0
    
        while head <= tail:
            mid = int((head + tail) / 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                head = mid + 1
            elif target < nums[mid]:
                tail = mid -1

        return -1

        