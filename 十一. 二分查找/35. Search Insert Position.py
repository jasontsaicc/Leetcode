"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


"""
class Solution:
    #     def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid -1
        return left

ans = Solution().searchInsert([1,3,5,6], 5)


"""
二分法來處理 先定義左右指針 在right ≥ left 的情況下 都會執行 
先找出一個中間的index((a+b)//2) 
當mid的值直接是target時 回傳 mid的index 
如果target 比 mid值還大的話 左邊+1 再來就右邊+1 最後回傳 left
"""