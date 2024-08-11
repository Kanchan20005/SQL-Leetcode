class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = len(nums)
        pre = [0]*a
        post = [0]*a
        for i in range(len(nums)):
            if i == 0:
                pre[i] =nums[i]
            else:
                pre[i] = pre[i-1]*nums[i]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post[i] =nums[i]
            else:
                post[i] = post[i+1]*nums[i]
        tR = [0]* a
        for i in range(len(nums)):
            if i ==0:
                tR[i] = post[1]
            elif i == len(nums)-1:
                tR[i] = pre[len(nums)-2]
            else:
                tR[i] = post[i+1]*pre[i-1]
        return tR 