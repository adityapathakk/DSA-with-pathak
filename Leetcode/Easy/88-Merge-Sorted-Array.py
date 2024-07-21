class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # while n > 0: Approach 1
        #     if nums1[m - 1] >= nums2[n - 1] and m > 0:
        #         nums1[m + n - 1] = nums1[m - 1]
        #         m -= 1
        #     else:
        #         nums1[m + n - 1] = nums2[n - 1]
        #         n -= 1

        # while n > 0: Approach 2
        #     nums1.pop(m)
        #     n -= 1

        # nums1[:] = nums1 + nums2
        # return nums1.sort()

        #for i in range(m + n - 1, n - 1, -1): Approach 3
        for i in (nums1[m:]):
            if i == 0:
                nums1.remove(0)
                
        nums1[:] = nums1 + nums2
        nums1.sort()

'''

tried a few different approaches :))


'''
