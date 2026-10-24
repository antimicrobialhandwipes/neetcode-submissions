class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        orig_len = len(nums)
        zeroed_list = []
        i = 0

        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
            else:
                i += 1

        
        for i in range((orig_len)-len(nums)):
            nums.append(0)
