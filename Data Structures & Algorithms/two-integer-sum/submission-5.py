class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_set:
                return [num_set[complement], i]
            else:
                num_set[num] = i
        return []