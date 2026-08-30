#1.type函数，用于检查一个变量或数据属于什么类型
age = 18
pi = 3.14
name = "Alice"
is_student = True

print(type(age))   # <class 'int'>
print(type(pi))    # <class 'float'>
print(type(name))  # <class 'str'>
print(type(is_student)) # <class 'bool'>

#2.类型转换：浮点转整数：直接截断小数部分（不是四舍五入）
a=1.99
b=int(a)
print(b)

#3.数字字符串转整数：字符串内容必须全是数字,如果是小数就报错
c=int("123")
print(c)

#4.整数转浮点：直接加上 .0
float(10)   # 结果 10.0

#5.数字字符串转浮点
float("3.14")  # 结果 3.14

#6.String 万物皆可转
str(100)      # 结果 "100"
str(True)     # 结果 "True"
str(3.14)     # 结果 "3.14"

#常用场景：输出拼接时，把数字和文字放在一起
age=18
print("我"+str(age)+"岁")

#易错点1
int("12.3")    # 报错！因为 "12.3" 是浮点数的写法，但 int() 要求纯整数文本，正确写法 int(float("12.3))
int("1a")      # 报错！因为含有字母
float("3.14.15") # 报错！因为小数点多了

#易错点2
num = 10
text = "个苹果"
# 错误写法: print(num + text)   # 报错
# 正确写法:
print(str(num) + text)  # 输出 "10个苹果"
print(num, text)        # 或者用逗号分隔，不用转换

#易错点3
int(True)   # 结果是 1
int(False)  # 结果是 0
#字符串非空，转为布尔值都是True
bool("")    # False (空字符串为False)
bool(" ")   # True (空格也是字符，非空)
bool("0")   # True (字符串"0"非空)