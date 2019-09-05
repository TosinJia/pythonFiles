"""
参考:https://www.jianshu.com/p/ffc93a407448
python 利用 redis 第三方库，首先安装

C:\\Users\\TosinJia>pip install redis
Collecting redis
  Downloading https://files.pythonhosted.org/packages/bd/64/b1e90af9bf0c7f6ef55e
46b81ab527b33b785824d65300bb65636534b530/redis-3.3.8-py2.py3-none-any.whl (66kB)

     |████████████████████            | 40kB 43kB/s eta 0:00
     |█████████████████████████       | 51kB 39kB/s eta
     |██████████████████████████████  | 61kB 46kB/
     |████████████████████████████████| 71kB 36k
B/s
Installing collected packages: redis
Successfully installed redis-3.3.8
WARNING: You are using pip version 19.2.2, however version 19.2.3 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' comm
and.

"""
import redis

# 配置严格模式 decode_responses https://www.jianshu.com/p/62e628f09b18
# 禁用原子性 transaction = False
r = redis.StrictRedis(host="192.168.1.121", port=6380, db=0, password='test', decode_responses=True)


# 连接池来操作
pool = redis.ConnectionPool(host="192.168.1.121", port=6380, db=0, password='test', decode_responses=True)
r = redis.Redis(connection_pool=pool)


# 管道
## 执行事务操作
r.set('pythontest', "test")
a = r.get("pythontest")
print(a)
pipe = r.pipeline()
pipe.set("pythontestpipe", "testpipe")
b = pipe.get("pythontestpipe")
print(b)
pipe.execute()
## 进行链式操作
pipe.set('testset', 'tset').sadd('testsadd', 'sadd').incr('auto_number').execute()


from redis.exceptions import WatchError
## WATCH 监控命令
watchKey = 'WATCH-KEY'
with r.pipeline() as pipe:
    while 1:
        try:
            # 设置一个 watch
            pipe.watch(watchKey)
            current_value = pipe.get(watchKey)
            if not bool(current_value):
                current_value = 0
            next_value = int(current_value)+1
            # 开始事务
            pipe.multi()
            pipe.set(watchKey, next_value)
            # 执行
            pipe.execute()
            break
            # 如果抛出 WatchError ，表示原子性失败
        except WatchError:
            # 另一个客户端修改了，我们必须重试
            continue
### 由于 Pipeline 在 watch 期间绑定到单个连接，必须调用 reset() 来确保返回连接池，使用 with 上下文的话，它会自动调用。当然也可以手动调用
pipe = r.pipeline()
while 1:
    try:
        pipe.watch(watchKey)
        current_value = pipe.get(watchKey)
        if not bool(current_value):
            current_value = 0
        next_value = int(current_value)+1
        pipe.multi()
        pipe.set(watchKey, next_value)
        pipe.execute()
        break
    except WatchError:
        continue
    finally:
        pipe.reset()

### transaction() 方法来简化操作
def client_side_incr(pipe):
    current_value = pipe.get(watchKey)
    if not bool(current_value):
        current_value = 0
    next_value = int(current_value) + 1
    pipe.multi()
    pipe.set(watchKey, next_value)
r.transaction(client_side_incr, watchKey)

# 迭代器
for key, value in(('A', '1'), ('B', '2'), ('C', '3')):
    r.set(key, value)

for key in r.scan_iter():
    print(str(key), str(r.get(key)))

