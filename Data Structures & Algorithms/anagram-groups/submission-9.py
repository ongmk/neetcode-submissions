
def getFrequencies(s: str) -> tuple[int]:
    freq = [0] * 26
    for char in s:
        index = ord(char) - ord('a')
        freq[index] += 1
    
    return tuple(freq)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            freq = getFrequencies(s)
            anagrams[freq].append(s)

        return list(anagrams.values())