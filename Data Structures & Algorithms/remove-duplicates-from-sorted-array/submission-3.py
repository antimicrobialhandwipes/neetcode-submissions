class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = sorted(set(nums))
        nums[:] = temp
        return len(temp)