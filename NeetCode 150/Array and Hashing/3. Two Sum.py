from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            invert = target-nums[i]
            if invert in seen:
                return list(sorted([seen[invert],i]))
            seen[nums[i]] = i
        
obj = Solution()
print(obj.twoSum([1,2,3],4))