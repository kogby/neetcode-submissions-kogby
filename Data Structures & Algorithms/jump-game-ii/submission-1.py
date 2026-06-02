class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     step_list = [float('inf')] * len(nums)
    #     step_list[0] = 0
    #     for ind in range(len(nums)):
    #         for step in range(1, nums[ind]+1):
    #             if ind + step < len(nums) and step_list[ind] + 1 < step_list[ind+step]:
    #                 step_list[ind+step] = step_list[ind] + 1
    #     return step_list[-1] 
    #     # Time O(mn), m = num_size, n = num list len
    #     # Space O(n)

    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0   # 用 jumps 次能到的最遠 index（這一層的右界）
        farthest = 0      # 從這一層任一點出發，下一跳能到的最遠
        for i in range(len(nums) - 1):   # 注意：不掃最後一格
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps