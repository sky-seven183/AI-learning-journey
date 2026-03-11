# # 集合  无序，不可重复，可修改的数据容器
# # 基本操作
# s1.add("t")                 添加元素到集合
# s1.remove("t")              移除指定元素（没有就报错）
# e = s1.pop()                随机删除元素并返回
# s1.clear()                  清空集合
# s1.difference(s2)           求差集
# s1.union(s2)                求并集
# s1.intersection(s2)         求交集
# # 定义
# s1 = {1,3,54,2,4,6,5,3,7}
# print(s1)
# print(type(s1))
# print()
# s2 = set()
# print(type(s2))
# print()
# s3 = {}
# print(type(s3))
# # 注意：空集合的定义不可以使用{}，{}表示空字典；由于集合无序，因此不支持下标索引访问
s1 = {1,2,3,4,5,6,7,8,9}
s1.add(10)
print(s1)
print()
#删除
s1.remove(1)
print(s1)
print()

e = s1.pop()
print(e)
print(s1)
print()

s1.clear()
print(s1)
print()
#集合操作
s2 = {"A","B","C"}
s3 = {"C","D","E"}
print(s2)
print(s3)
print(s2.difference(s3))
print(s3.difference(s2))
print(s2.union(s3))
print(s2.intersection(s3))
