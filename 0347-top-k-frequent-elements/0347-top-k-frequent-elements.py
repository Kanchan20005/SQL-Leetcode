class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = {}
        maxn = 0
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            counters[n] = 1 +counters.get(n,0)
        for n, c in counters.items():
            freq[c].append(n)
            if c > maxn:
                maxn = c
        res = []
        for i in range(maxn, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        