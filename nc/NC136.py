# -*- coding: utf-8 -*-
# author = "Louis"
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, xianxu, zhongxu):
        # write code here
        if not xianxu or not zhongxu or len(xianxu) != len(zhongxu):
            return []
        result = []
        root = self.rebuild(xianxu, zhongxu)
        queue = [root]
        while queue:
            result.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return result

    def rebuild(self, xianxu, zhongxu):
        if not xianxu or not zhongxu or len(xianxu) != len(zhongxu):
            return None
        root = TreeNode(xianxu[0])
        left_len = zhongxu.index(root.val)
        root.left = self.rebuild(xianxu[1:left_len + 1], zhongxu[:left_len])
        root.right = self.rebuild(xianxu[left_len + 1:], zhongxu[left_len + 1:])
        return root

if __name__ == '__main__':
    a = [1,2,4,5,3]
    b = [4,2,5,1,3]
    head = Solution().solve(a, b)
    print(1)
