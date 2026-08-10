def getFrequencies(s: str) -> dict[str, int]:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    return freq

class Solution:
        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = getFrequencies(s)
        t_freq = getFrequencies(t)

        return s_freq == t_freq