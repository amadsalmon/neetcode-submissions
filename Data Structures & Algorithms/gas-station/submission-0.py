class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0: 
            return -1

        n = len(gas)
        i = 0
        while i < n:
            if gas[i] - cost[i] < 0:
                i += 1
            else:
                running_balance = 0
                j = i
                while j < n and running_balance >= 0:
                    running_balance += gas[j] - cost[j]
                    j += 1
                if j == n:
                    return i
                elif running_balance < 0:
                    i = j

        return i        

"""
DRY RUN TEST

gas=[1,2,3,4] sum = 10
cost=[2,2,4,1] sum = 9 -> difference is 1, there is a solution.

i = 0 , net = 1-2=-1, skip, i+=1
i = 1: net = 0, enter while:
    running_balance =0, j=1 
    enter while :
        running_balance += 0 = 0, j+= 1 = 2
        running_balance += -1 = -1 
    while exits because running_balance<0
    j != n (2!=4), else: running balance <0 true, so i = j+1 = 3

continue while at i = 3
    net = 4-1=3 >0
    running_balance = 0
    j = i = 3
    enter while:
        r_b += 3
        j +=1 = 4
    exit while because j == 4
    if j==n (4==4): return i = 3

returns 3


Correct
"""