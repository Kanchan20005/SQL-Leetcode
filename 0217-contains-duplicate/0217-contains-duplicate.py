class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        diction = set()
        for i in nums:
            if i in diction:
                return True   
            else:
                diction.add(i)
        return False