class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1

        while head <= tail:
            mid = int((head+ tail) / 2)

            if nums[mid] == target:
                return mid

            if nums[head] <= nums[mid]:
                if target > nums[mid] or target < nums[head]:
                    head = mid + 1
                else:
                    tail = mid - 1
            else:
                if target < nums[mid] or target > nums[head]:
                    tail = mid - 1
                else:
                    head = mid + 1
                            
        return -1