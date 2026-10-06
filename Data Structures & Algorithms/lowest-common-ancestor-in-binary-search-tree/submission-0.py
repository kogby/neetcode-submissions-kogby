# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return right if we only found right
        # return left if we only found left 
        # return root if we found each in left/right
        def dfs(node):
            if not node:
                return None
            print(node.val)
            if node == p or node == q:
                return node

            left_result = dfs(node.left)
            right_result = dfs(node.right)
            # print(left_result)
            # print(right_result)
            if left_result and right_result:
                return node
            elif left_result:
                return left_result
            elif right_result:
                return right_result
            else:
                return None

        
        return dfs(root)
            


        

