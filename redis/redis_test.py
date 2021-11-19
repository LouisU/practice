# -*- coding: utf-8 -*-
# author = "Louis"
import redis

def getconn():

    rds_conpl_config = redis.ConnectionPool(host="106.52.206.213", port=6379, max_connections=10)
    rds_conpl = redis.Redis(connection_pool=rds_conpl_config)

    return rds_conpl








if __name__ == '__main__':
    # rs = redis.StrictRedis(host="106.52.206.213", port=6379)
    # value = rs.get("hello")
    for i in range(11):
        print(i)
        re = getconn().get_connection
    print(value)
