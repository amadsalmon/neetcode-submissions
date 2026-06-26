def updateFreq(letter, freq_dict):
    if letter not in freq_dict:
        freq_dict[letter] = 1
    else:
        freq_dict[letter] = freq_dict[letter] + 1
    return freq_dict

class Solution:
    """
    New attempt. That's O(n) in complexity. 
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        s_frequencies = {}
        t_frequencies = {}

        for i in range(0, len(s)):
            s_frequencies = updateFreq(s[i], s_frequencies)
            t_frequencies = updateFreq(t[i], t_frequencies)
            
        # Compare both frequency dictionaries
        for letter, frequency in s_frequencies.items():
            if (letter not in t_frequencies) or (t_frequencies[letter] != frequency): 
                return False

        return True

    """
    Original attempt. That's O(n^2) in complexity. 
    """
    def isAnagram_initial_solution(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        t_copy = t
        for letter in s:
            if letter in t_copy:
                t_copy = t_copy.replace(letter, '', 1)
            else:
                return False
        return True
        

        