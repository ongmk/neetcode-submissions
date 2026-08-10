
def getFrequencies(s: str) -> tuple[int]:
    freq = [0] * 26
    for char in s:
        index = ord(char) - ord('a')
        freq[index] += 1
    
    return tuple(freq)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams: dict[tuple[int], list[str]] = {}

        for s in strs:
            freq = getFrequencies(s)

            if freq in anagrams:
                anagrams[freq].append(s)
            else:
                anagrams[freq] = [s]
        
        return list(anagrams.values())