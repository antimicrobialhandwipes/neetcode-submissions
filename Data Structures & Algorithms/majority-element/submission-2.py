class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}

        for item in nums:
            hash_table[item] = hash_table.get(item, 0) + 1

        return max(hash_table, key=hash_table.get)