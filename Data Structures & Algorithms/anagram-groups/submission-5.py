from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            key = str(sorted(word))
            seen[key].append(word)
        return list(seen.values())

        