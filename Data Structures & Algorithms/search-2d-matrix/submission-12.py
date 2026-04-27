class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nearestMax = 0
        myRow = []
        
        for element in matrix:
            
            if element[-1] >= target:
                myRow = element
                break
            
            
        if not myRow:
            return False

        head = 0
        tail = len(myRow) - 1

        while head <= tail:
            mid = int((head + tail) / 2)

            if myRow[mid] == target:
                return True
            elif myRow[mid] >= target:
                tail = mid - 1
            elif myRow[mid] < target:
                head = mid + 1

        return False