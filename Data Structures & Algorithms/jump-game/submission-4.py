class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     # a list to store the status of whether I can jump to this point or not
    #     can_jump = [0] * len(nums)
    #     can_jump[0] = 1
    #     for ind in range(len(nums)):
    #         if can_jump[ind] == 1:
    #             # update if I can go there
    #             for step in range(ind, ind + nums[ind]+1):
    #                 if step < len(nums):
    #                     can_jump[step] = 1

    #     return can_jump[-1] == 1

    # This is O(n^2), I reocrd every place status.

    # For O(n) and O(1) space:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:       # 這個位置根本到不了，直接失敗
                return False
            max_reach = max(max_reach, i + nums[i])
        return True