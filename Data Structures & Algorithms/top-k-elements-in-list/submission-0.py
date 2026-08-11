class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        out = []
        for n, f in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            out.append(n)
            if len(out) == k:
                return out
        return out