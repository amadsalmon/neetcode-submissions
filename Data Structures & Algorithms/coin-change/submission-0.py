INF = 2**31 - 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None] * (amount + 1)
        memo[0] = 0

        def helper(rem: int) -> int:
            if memo[rem] is not None:
                return memo[rem]
            
            possible_coins = [coin for coin in coins if coin <= rem]
            if possible_coins:
                memo[rem] = min([helper(rem - coin) for coin in possible_coins]) + 1
            else:
                memo[rem] = INF
                
            return memo[rem]

        result = helper(amount)
        return -1 if result >= INF else result

"""

        1,2,5
        amount= 11
        
        Initial:
        [0,1,1,0,0,1,0,0,0,0,0,0]
         0 1 2 3 4 5 6 7 8 9 10 11

        Final:
        [0,1,1,2,2,1,2,2,3,3,2,3]
         0 1 2 3 4 5 6 7 8 9 10 11

         helper(11) -> 1 + min(
            helper(11-1=10) -> 1 + min(
                helper(10-1=9) -> 1 + min(
                    helper(9-1=8) -> 1 + min(
                        helper(8-1=7) -> 1 + min(
                            helper(7-1=6) -> 1 + min(
                                helper(6-1=5) -> 1
                                helper(6-2=4) -> 1 + min(
                                    helper(4-1=3) -> 
                                        1 + min(
                                        helper(3-1=2) -> 1
                                        helper(3-2=1) -> 1
                                        helper(3-5=-2) -> IMPOSSIBLE
                                    ) = 2
                                    helper(4-2=2) -> 1
                                    helper(4-5=-1) -> IMPOSSIBLE
                                ) = 1+1 = 2
                                helper(6-5=1) -> 1
                            ) = 1 + 1 = 2 
                            helper(7-2=5) -> 1
                            helper(7-5=2) -> 1
                        )
                        helper(8-2=6), -> 2
                        helper(8-5=3), -> 2
                    ) -> 2 + 1 = 3
                    helper(9-2=7),-> 2
                    helper(9-5=4),-> 2
                ) -> 2 + 1 = 3
                helper(10-2=8), -> 3
                helper(10-5=5), -> 1
            ) -> 1 + 1 = 2
            helper(11-2=9), -> 3
            helper(11-5=6), -> 2
         ) -> 2 + 1 = 3
         ---> 3
"""