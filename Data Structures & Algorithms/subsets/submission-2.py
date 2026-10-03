class Solution:
    """
    Backtracking solution
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        index = 0

        def backtrack(index: int, current_path: List[int]) -> None:
            # Base case
            if index == len(nums):
                res.append(current_path.copy())
                return
            
            # Decision 1: take current number
            current_path.append(nums[index])
            backtrack(index + 1, current_path)
            
            # Go back
            current_path.pop()

            # Decision 2: skip current number
            backtrack(index + 1, current_path)
        
        backtrack(0, [])
        return res

    """
    Iterative solution
    """
    def subsets_iterative(self, nums: List[int]) -> List[List[int]]:
        all_sets = [set()]

        for n in nums:
            all_sets_snapshot = all_sets.copy()
            for s in all_sets_snapshot:
                new_set = s.copy()
                new_set.add(n)
                all_sets.append(
                    new_set
                )
        
        return [list(s) for s in all_sets]