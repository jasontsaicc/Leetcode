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
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 定義target在左閉右閉的區間裡，[left, right]
        left, right = 0, len(nums) - 1
        # 當left==right，區間[left, right]依然有效
        while left <= right:
            # 防止溢出 等同於(left + right)/2
            mid = (left + right) // 2
            # target 在左區間，所以[left, middle - 1]
            if nums[mid] > target:
                right = mid -1
            # target 在右區間，所以[middle + 1, right]
            elif nums[mid] < target:
                left = mid +1
            else:
                return mid
        """ 分別處理如下四種情況
            目標值在數組所有元素之前  [0, -1]
            目標值等於數組中某一個元素  return middle;
            目標值插入數組中的位置 [left, right]，return  right + 1
            目標值在數組所有元素之後的情況 [left, right]， 因為是右閉區間，所以 return right + 1
            
        """

        return right +1

ans = Solution().searchInsert([1,3,5,6], 5)


"""
二分法來處理 先定義左右指針 在right ≥ left 的情況下 都會執行 
先找出一個中間的index((a+b)//2) 
當mid的值直接是target時 回傳 mid的index 
如果target 比 mid值還大的話 左邊+1 再來就右邊+1 最後回傳 left
"""