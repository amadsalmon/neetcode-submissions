class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:        
        res = []

        def backtrack(index: int, elements: List[int], remaining: int) -> None:
            if remaining == 0:
                res.append(list(elements))
                return
            elif index == len(nums) or remaining < 0:
                return

            # Include
            n = nums[index]
            elements.append(n)
            backtrack(index, elements, remaining - n)

            # Exclude
            elements.pop()
            backtrack(index + 1, elements, remaining)
        
        backtrack(0, [], target)

        return res
