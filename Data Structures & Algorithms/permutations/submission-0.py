class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        path = []
        used = [False] * len(nums)        

        def backtrack():
            # found a permutation here
            if len(path) == len(nums):
                results.append(path[:])
                # return
            # pick a number
            for i in range(len(nums)):
                # can't used this
                if used[i] == True:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                used[i] = False
                path.pop()

        backtrack()

        return results
