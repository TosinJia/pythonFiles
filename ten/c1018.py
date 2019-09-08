# 序列化
import json

# JSON Object
student = {'name': 'tosin', 'age': 20, 'flag': True}
json_str = json.dumps(student)
print(json_str, type(json_str))

# JSON Array
student_list = [
                    {'name': 'tosin', 'age': 20, 'flag': True},
                    {'name': 'tosin1', 'age': 21}
            ]
json_str = json.dumps(student_list)
print(json_str, type(json_str))
# NoSQL数据库 MongoDB 适合存储序列化后的对象，强烈反对把对象序列化后以字符串形式存入数据库
