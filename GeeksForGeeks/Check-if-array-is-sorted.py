class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # return arr == sorted(arr)
        for i in range(1, len(arr)):
            if not (arr[i] >= arr[i - 1]):
                return False
        return True