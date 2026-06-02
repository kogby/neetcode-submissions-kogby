class Solution:
    def jump(self, nums: List[int]) -> int:
        step_list = [float('inf')] * len(nums)
        step_list[0] = 0
        for ind in range(len(nums)):
            for step in range(1, nums[ind]+1):
                if ind + step < len(nums) and step_list[ind] + 1 < step_list[ind+step]:
                    step_list[ind+step] = step_list[ind] + 1
        return step_list[-1] 