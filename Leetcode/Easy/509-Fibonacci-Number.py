class Solution: # most optimised way (bottom - up : since we start from the first cases and reach Nth position, i.e. the answer)
    def fib(self, n: int) -> int:
        if n < 2: # base case
            return n
        
        prev2, prev1 = 0, 1
        for _ in range(1, n):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr
        
        return curr

# apart from this, there're two top-down approaches (we go back from the answer to the base cases)
    # the recursive way - the answer will be fib(n - 1) + fib(n - 2)
    # to increase efficiency, there's the DP way - initialise a DP array and store the values of all the sub-problems that we encounter.