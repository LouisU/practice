# -*- coding: utf-8 -*-
# author = "Louis"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        root.left, root.right = self.mirrorTree(root.right),self.mirrorTree(root.left)
        return root

if __name__ == '__main__':
    pass
