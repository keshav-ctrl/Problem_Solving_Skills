from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index
        return []

S_Object = Solution()

print(S_Object.twoSum([2, 7, 11, 15], 9)) 
# expected out come is [0,1]
print(S_Object.twoSum([2, 7, 11, 15], 12))
# expected out come is []
print(S_Object.twoSum([2, 7, 11, 15], 22))
# expected out come is[1,3]