#（一）列表[] 第一个索引是0,接着依次是1,2
list = [1,2,3,4,5]
list.append(6)   #添加元素6到列表末尾
print("添加加元素后：",list)

list = [1,'fibos',3,'baidu',5]
list.insert(0,7) #在列表索引位置0添加元素7；
print("索引位置新加元素后：",list)

list = [1,'fibos',3,'baidu',5,5]
list.count(5)    #统计元素在列表中出现的次数
print("5出现的次数：",list.count(5))

list = [1,'fibos',3,'baidu',4,5]
list.remove('baidu')  #移除任意指定值
print("新列表：",list)

list = [1,'fibos',3,'baidu',4,5]
list.reverse()  #将列表元素进行反向排序
print("列表翻转后：",list)

list = [1,4,3,12,9,8]
list.sort()  #给列表排序，排序前提是元素是可比较的
print("排序后的结果：",list)

list = [1,'fibos',3,'baidu',5]
del list[2]
print("删除第2个元素后：",list) #删除列表中的元素

list = [1,'fibos',3,'baidu',5]
list.pop(0)     #移除列表中指定的元素（默认移除最后一个元素），并且返回该元素的值
print("移除元素后：",list)

#（二）列表推导式的使用
list = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(list)    #列表推导式
list = [x*y for x in range(1,5) for y in range(1,4) if x > y]
print(list)     #结构：在一个中括号里包含一个表达式，然后是一个for语句，然后是0个或多个for或者if语句
                #执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边第一条语句是最后一层
