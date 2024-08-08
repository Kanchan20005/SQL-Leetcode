class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        diction = {}
        for i in nums:
            if i not in diction:
                diction[i] = 1
            else:
                return True
                diction[i] = diction[i]+1
        return False