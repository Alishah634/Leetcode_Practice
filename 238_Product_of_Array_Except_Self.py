print(f'''
238. Product of Array Except Self
Medium
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

''')

import termcolor

class Solution:
    def productExceptSelf(self, nums):
        prefix = 1
        res = [1 for _ in nums]
        for i, num in enumerate(nums):
            res[i] *= prefix
            prefix *= num
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

if __name__ == "__main__":    
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
    ]

    solution = Solution()

    for nums, expected in test_cases:
        result = solution.productExceptSelf(nums)
        test_result = termcolor.colored("Pass", "green") if result == expected else termcolor.colored("Fail", "red")
        print(termcolor.colored(f"Input: \nnums: {nums}\n", 'cyan'))
        print(f"Output: {result}, Result: {test_result}\n")
