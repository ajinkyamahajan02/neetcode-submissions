class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2 
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)

        while True:

            i = (l + r) // 2
            j = half - i

            Aleft = A[i-1] if i > 0 else float("-infinity")
            Aright = A[i] if (i) < len(A) else float("infinity")

            Bleft = B[j-1] if j > 0 else float("-infinity")
            Bright = B[j] if (j) < len(B) else float("infinity")

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)


            elif Aleft > Bright:
                r -= 1
            else:
                l += 1

        

