### Two Sum Problem Solution with Execution Time Measurement from the Letcode platform

# 1st- method

import time

nums = [2, 3, 5]
target = 8

start = time.time()

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

end = time.time()

print(Solution().twoSum(nums, target))
print("Execution Time: ", end - start)
