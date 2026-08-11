class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums))]

        for n in nums:
            freq[n] += 1
        
        for number, frequency in freq.items():
            buckets[frequency-1].append(number)

        out = []
        for ls in buckets[::-1]:
            for n in ls:
                out.append(n)
                if len(out) == k:
                    return out
        
        return out