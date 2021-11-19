# -*- coding: utf-8 -*-
# author = "Louis"
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "node: {}".format(self.val)


# class Solution:
#     def __init__(self):
#         self.dic = {}
#         self.res = []
#
#     def zigzagLevelOrder(self, root, d=0):
#         # write code here
#         self.go(root)
#         for k in sorted(self.dic.keys()):
#             self.res.append(self.dic[k])
#         return self.res
#
#     def go(self, root, d=0):
#         if root is None:
#             return
#         d += 1
#         res = []
#         if d % 2 == 1:
#             res.append(root.left)
#             res.append(root.right)
#         else:
#             res.append(root.right)
#             res.append(root.left)
#
#         if d not in self.dic:
#             self.dic[d] = [root.val]
#         else:
#             self.dic[d].append(root.val)
#         while len(res):
#             self.go(res.pop(), d)
# class Solution:
#     def __init__(self):
#         self.dic = {}
#         self.res = []
#
#     def zigzagLevelOrder(self, root, d=0):
#         # write code here
#         self.go(root)
#         for k in sorted(self.dic.keys()):
#             self.res.append(self.dic[k])
#         return self.res
#
#     def go(self, root, d=0):
#         if root is None:
#             return
#         d += 1
#         if d not in self.dic:
#             self.dic[d] = [root.val]
#         else:
#             self.dic[d].append(root.val)
#         if d % 2 == 1:
#             self.go(root.right, d)
#             self.go(root.left, d)
#         else:
#             self.go(root.left, d)
#             self.go(root.right, d)
class Solution:
    def zigzagLevelOrder(self, root, d=0):
        # write code here
        if root is None:
            return []
        res = []
        cur_level = []
        cur_level.append(root)
        next_level = []
        cur_level_value_list = []
        d = 1
        while len(cur_level):
            node = cur_level.pop()
            cur_level_value_list.append(node.val)
            if d % 2 == 1:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            else:
                if node.right is not None:
                    next_level.append(node.right)
                if node.left is not None:
                    next_level.append(node.left)

            if not cur_level:
                cur_level += next_level
                next_level = []
                d += 1
                res.append(cur_level_value_list)
                cur_level_value_list = []
        return res


if __name__ == '__main__':
    node = TreeNode(1)
    head = node
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    print(Solution().zigzagLevelOrder(head))
