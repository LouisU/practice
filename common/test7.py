# -*- coding: utf-8 -*-
# author = "Louis"

# 标题：服务循环依赖检测
# 描述信息
# 在微服务的架构下，公司内部会有非常多的独立服务。
# 服务之间可以相互调用，往往大型应用调用链条很长，如果出现循环依赖将出现非常恶劣的影响。
# 对于一个具体应用，已知各个服务的调用关系（即依赖关系），请判断是否存在循环调用。
# 输入：
# 一组服务依赖关系list，('A', 'B') 表示 A 会调用 B 服务
# service_relations = [('A', 'C'), ('B', 'D'), ('D', 'A')]
# 输出：
# 由于存在 A - B - D - A 故存在循环依赖，返回True；反之如果不存在，返回False


class Solution:

    arr = []

    def check_relation(self, service_relations):
        k, v = service_relations[0]
        return self.check_relationR(k, v, service_relations[1:])


    def check_relationR(self, k, v, service_relations):
        # service_relations第一个元素 和 后面的(n-1)个元素是否形成循环调用
        if v in self.arr:
            return True
        else:
            for key, value in service_relations:
                if key == v:
                    pass
        k, v = service_relations[0]
        self.check_relationR(k, v, service_relations[1:])





if __name__ == '__main__':
    pass
