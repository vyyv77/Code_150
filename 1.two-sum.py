from typing import List
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present_number_index = 0
        for i in nums:
            inner_index = 0
            for next in nums:
                if present_number_index == inner_index:
                    inner_index += 1
                    continue
                else :
                    if target == next + i:
                        return [present_number_index, inner_index]
                        
                    else:
                        inner_index += 1
                        continue
            present_number_index += 1        
# @lc code=end

