class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = nums
        b = set(nums)
        if len(a) != len(b):
            return True
        else:
            return False