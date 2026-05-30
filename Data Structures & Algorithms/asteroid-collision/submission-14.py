class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Brute Force: Scan O(n^2)
        # Stack: O(n)
        stack = []
        for num in asteroids:
            while stack and num < 0 < stack[-1]:
                if stack[-1] < abs(num):
                    stack.pop()
                elif stack[-1] == abs(num):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(num)
        return stack