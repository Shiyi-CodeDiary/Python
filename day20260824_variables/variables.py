a=1
b='a'
score=10.5
is_stu=False#不能写成true和false,首字母要大写
print(a,b,score,is_stu)

# 等号左右数量要一致
x,y,z=1,2,3
print(x,y,z)

#交换变量值
m,n=1,2
m,n=n,m #交换
print(m,n) # 1 2

name='张三'
city="北京"
multi_line = """这是
多行字符串"""
empty='' #空字符串
print(name,city,empty,multi_line)

#列表（多个值）
scores = [90, 85, 88, 92]           # 整数列表
names = ["小明", "小红", "小刚"]     # 字符串列表
mixed = [1, "hello", 3.14, True]   # 混合类型
empty_list = []                     # 空列表

#字典（键值对）
person = {"name": "张三", "age": 25, "city": "北京"}
student = {"id": 1001, "score": 95, "is_pass": True}
empty_dict = {}

#元组（不可变）
coordinates = (10, 20)              # 坐标
colors = ("red", "green", "blue")   # 颜色
single_item = (5,)                  # 单个元素要加逗号

#集合（去重）
tags = {"python", "java", "c++"}    # 不重复元素
numbers = {1, 2, 3, 4, 5}
empty_set = set()                   # 注意：{} 是空字典
print(empty_set)