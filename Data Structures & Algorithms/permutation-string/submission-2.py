class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freqs = defaultdict(int)
        for letter in s1:
            freqs[letter] += 1

        print(freqs)

        for i in range(0, len(s2)-len(s1)+1):
            print(f"{s2[i]}")
            if s2[i] in freqs:
                print(f"  {s2[i]} in freqs")
                matched_completely = True
                copy = freqs.copy()
                j = i
                for j in range(i, i + len(s1)):
                    if s2[j] in copy and copy[s2[j]] > 0:
                        print(f"      {s2[j]} in copy")
                        copy[s2[j]] -= 1
                    else:
                        print(f"      {s2[j]} NOT in copy")
                        matched_completely = False
                        break
                if matched_completely: return True
        
        return False
                    
        