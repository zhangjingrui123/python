#集合 {}  无序不重复元素的集，用大括号/set{}创建集合；创建空集合要用set()
set = {'dapp','fibos','otc','python','otc'}
print(set)

set = {'dapp','fibos','otc','python','otc'}
set.add('1')     #添加元素到集合中
print(set)

set = {'dapp','fibos','otc','python','otc'}
set.update({2,3})  #添加元素的参数可以是：列表，元组，字典
print(set)

set = {'dapp','fibos','otc','python','otc'}
set.remove('otc')    #移除元素
print(set)

set = {'dapp','fibos','otc','python','otc'}
len(set)             #计算集合元素个数
x = len(set)
print(x)
