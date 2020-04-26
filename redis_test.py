import redis

#定义地址和端口
host = '127.0.0.1'
port = 6379

#建立redis连接
r = redis.Redis(host=host,port=port)

# 列表操作
r.lpush('123',1)

# 过期时间
r.expire('123',30)
# 打印过期时间
print(r.ttl('liuyue'))
# 打印列表长度
print(r.llen('123'))



if r.llen('123') > 5:
    print('您的账号被锁定')

#声明一个值
# r.set('test','123')

#取值
# code = r.get('test')

#转码
# code = code.decode('utf-8')

# print(code)