# 反序列化
import json

# # JSON Object
json_str = "{name: tosin, age:20}"
# key、字符串要用双引号括起来
json_str = '{"name": "tosin", "age":20}'
student = json.loads(json_str)
# json字符串转换为python里的字典
print(student, type(student))
print(student["name"], student["age"])

# JSON Array
json_str = '[{"name": "tosin", "age":20, "flag":false},{"name": "tosin1", "age":21}]'
studentList = json.loads(json_str)
# json字符串转换为python里的字典
print(studentList, type(studentList))
print(studentList[0]["name"])
