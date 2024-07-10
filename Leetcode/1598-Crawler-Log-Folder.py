class Solution: # Brute Force Approach
    def minOperations(self, logs: List[str]) -> int:
        minOperations = 0

        for log in logs:
            if log == "../":
                if minOperations > 0:
                    minOperations -= 1
                else:
                    continue
            elif log == "./":
                continue
            else:
                minOperations += 1
        
        return minOperations

''' Approach

-> if the log is anything apart from ../ or ./, then it means we're entering a new folder that we'll need to exit - so we add 1 to the minimum operations.
-> if the log is ../, then we moved back to a parent folder. that's one less folder we have to exit, so we subtract 1 from minimum operations (except when the minimum operations is already 0, in that case we just continue).
-> if the log is ./, then there isn't any operation. no folder was changed, so we simply continue.

'''
