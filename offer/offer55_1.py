# -*- coding: utf-8 -*-
# author = "Louis"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init__(self):
    #     self.max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        d = 1
        return max(d+self.maxDepth(root.left), d+self.maxDepth(root.right))

if __name__ == '__main__':
    pass
