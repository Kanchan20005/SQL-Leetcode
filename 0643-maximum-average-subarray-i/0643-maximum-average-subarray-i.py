class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        winsum = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            winsum += nums[i]
            if i-start +1== k:
                maxSum = max(maxSum, winsum/k)
                winsum = winsum - nums[start]
                start = start +1
        return maxSum