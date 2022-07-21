memo = {}

def l(nums, i):
    if i in memo:
        return memo[i]

    # last number
    if i == len(nums) - 1:
        return 1

    max_len = 1
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(max_len, l(nums, j) +1 )
    memo[i] = max_len

    return max_len
def lenght_of_LTS(nums):
    return max(
        l(nums, i) for i in range(len(nums))
    )

nums = [1, 5, 2, 4, 3]
print(lenght_of_LTS(nums))