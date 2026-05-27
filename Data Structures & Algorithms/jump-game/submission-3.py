class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # a list to store the status of whether I can jump to this point or not
        can_jump = [0] * len(nums)
        can_jump[0] = 1
        for ind in range(len(nums)):
            if can_jump[ind] == 1:
                # update if I can go there
                for step in range(ind, ind + nums[ind]+1):
                    if step < len(nums):
                        can_jump[step] = 1

        return can_jump[-1] == 1