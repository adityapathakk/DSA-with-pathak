class Solution: # simulate the circle - keep removing the last friend until circle has 1 friend left, i.e. the winner.
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [friend for friend in range(1, n + 1)]
        index = 0

        while len(friends) != 1: # when length = 1, only the winner is left in the circle.
            remove = (index + k - 1) % len(friends)
            friends.pop(remove)
            index = remove
        
        return friends[0]
         
''' Optimised Approach: Bottom-up DP: [winner(n, k); winner(n + 1, k + 1) = (winner(n, k) + k) % (n + 1]

        winner = 0

        for friend in range(1, n + 1):
            winner = (winner + k) % friend

        return winner + 1

'''
