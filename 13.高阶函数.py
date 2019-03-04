#高阶函数：一个函数可以作为参数传给另一个函数/一个函数的返回值为另一个函数本身
#（一）map函数：接受一个函数和一个序列（迭代器）作为输入，对序列的每一个值应用这个函数，返回一个新的序列
def f(x):
    return x * x
ret = map(f,[1,2,3,4])           #接受2个参数：1个函数和1个序列,map将传入的函数依次作用到序列[1,2,3,4]的每个元素
ret = list(ret)                  #将map返回的结果转换成新的list集合返回(因为在Python3中返回的是迭代器)
print(ret)
#(二)reduce函数：对序列内所有元素进行累计操作
from functools import reduce     #reduce在Python3中不是内置函数，需要从functools中导入
def add(a,b):
    return a + b
ret = reduce(add,[1,2,3,4])      #reduce把一个函数作用在一个序列[1,2,3,4]上，
print(ret)                       #这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做计算。

from functools import reduce
def f(x,y):
    return x * y
ret = reduce(f,range(1,4))       #reduce(f,(1,4))=f(f(1,2),3)
print(ret)
#(三)filter函数：接受一个函数和一个序列，把传入的参数依次作用于每个元素，根据返回值是：ture还是flase决定保留/丢弃元素
def f(x):
    return x %2 == 0             #能被2整除
ret = filter(f,range(1,5))       #过滤掉[1,2,3,4]中不能被2整除的元素
ret = list(ret)                  #将返回的结果转换成新的list（Python3返回结果是迭代器）
print(ret)
#（四）sorted函数：对原可迭代对象进行排序,语法：sorted（可迭代对象[cmp[key[reverse]]]）
list = [-12,2,-20,6,1,18]        #Python3取消了对cmp的支持
print(sorted(list))              #key接受一个函数，这个函数只接受一个元素，默认为none
                                 
print(sorted(list,key=abs))      #key=abs(按绝对值大小进行排序)
list = ["Python","JAVA","C"]
print(sorted(list,key=str.lower))
print(sorted(list,reverse=False))  #reverse是一个布尔值，如果设置为true，列表元素被倒叙排列，默认为false







