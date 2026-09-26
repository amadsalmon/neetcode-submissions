class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            key = str(sorted(word))
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]
        return list(seen.values())

        