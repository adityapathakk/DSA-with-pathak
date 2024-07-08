class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        timeForOnePass = (2 * n) - 2 # from 1 to n, in n - 1 seconds. from n to 1, in n - 1 seconds.
        if time < timeForOnePass:
            if time < n - 1: # going forward (1 to n)
                return time + 1 # 0 based indexing
            return (n - (time % (n - 1))) # going backward (n to 1)
        else:
            remainder = time % timeForOnePass # to avoid calculating unnecessary pillow passes
            if remainder < n - 1: # going forward (1 to n)
                return remainder + 1 # 0 based indexing
            return (n - (remainder % (n - 1))) # going backward (n to 1)
