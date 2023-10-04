from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]:    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > target:
                continue
            if nums[i] + nums[j] == target:
                ans = [i , j]
                return ans         
    return