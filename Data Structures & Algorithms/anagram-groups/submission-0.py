class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createFreqTupleForWord(word: string) -> tuple:
            arr = [0]*26
            for letter in word:
                pos = ord(letter) - 97
                arr[pos] += 1
            return tuple(arr)
        
        seen_freqs = {}

        for word in strs:
            freqs = createFreqTupleForWord(word)
            if freqs in seen_freqs:
                seen_freqs[freqs].append(word)
            else:
                seen_freqs[freqs] = [word]

        groups = []
        for x in seen_freqs.values():
            groups.append(x)

        return groups


        