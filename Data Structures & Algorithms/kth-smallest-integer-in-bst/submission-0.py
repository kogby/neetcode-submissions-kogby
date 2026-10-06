# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None

        def inorder(node):
            nonlocal count, answer
            if node is None or answer is not None:
                return

            inorder(node.left)              # 左

            if answer is not None:          # 左子樹已經找到答案，不用再往下做
                return
            count += 1                      # 中：拜訪到第 count 小的節點
            if count == k:
                answer = node.val
                return

            inorder(node.right)             # 右

        inorder(root)
        return answer