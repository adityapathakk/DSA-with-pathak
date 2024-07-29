class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total = 0
        n = len(rating)
        
        for i in range(n):
            right_less = 0
            right_more = 0
            left_less = 0
            left_more = 0

            # counting soldiers after i
            for j in range(i + 1, n):
                if rating[j] < rating[i]:
                    right_less += 1
                elif rating[j] > rating[i]:
                    right_more += 1
            
            # counting soldiers before i
            for j in range(i):
                if rating[j] < rating[i]:
                    left_less += 1
                elif rating[j] > rating[i]:
                    left_more += 1

            # calculating total number of valid teams
            total += right_less * left_more + right_more * left_less

        return total       

''' Approach

revise from here
https://leetcode.com/problems/count-number-of-teams/solutions/5551415/beats-100-c-py-java-go-simple

'''
