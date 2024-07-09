class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time, wait, numOfCustomers = 0, 0, len(customers)
        for i in range(numOfCustomers):
            arrivalTime, orderTime = customers[i][0], customers[i][1]

            if time >= arrivalTime:
                time += orderTime
            else:
                time = arrivalTime + orderTime
            wait += time - arrivalTime
        
        return wait / numOfCustomers

''' Approach

initialise few variables:
-> running time - time
-> waiting time of each customer - wait
-> arrival time of the customer - arrivalTime
-> order preparation time of the customer - orderTime

iterating over the customers list, check if the running time is past the arrival time of current customer, or before:
-> if it's past the arrival time of current customer, then chef is available. so, just add preparation time to running time.
-> if it's before the arrival time of current customer, then chef has to wait for customer to arrive before preparing the order. so, running time is set to arrival time + order preparation time.
the wait variable is updated at the end of each iteration - difference between the time their order was prepared and the time they arrived.

leetcode solutions post: https://leetcode.com/problems/average-waiting-time/solutions/5448796/super-easy-detailed-explanation-python-solution/

'''
