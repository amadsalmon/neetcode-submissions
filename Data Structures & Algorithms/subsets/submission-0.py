class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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