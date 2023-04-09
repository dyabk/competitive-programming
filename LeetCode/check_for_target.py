def check_for_target(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        curr = nums[l] + nums[r]
        if curr == target:
            return True
        if curr > target:
            r -= 1
        else:
            l += 1

    return False
