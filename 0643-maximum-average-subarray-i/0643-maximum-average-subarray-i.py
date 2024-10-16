class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        winAvg = maxAvg = sum(nums[:k])/k
        for i in range(0,len(nums)-k,1):
            winAvg = winAvg - nums[i]/k + nums[i+k]/k
            maxAvg = max(maxAvg, winAvg)

        return maxAvg