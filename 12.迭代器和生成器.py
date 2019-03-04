#迭代器和生成器
#（一）迭代器的2个基本方法：iter()和next()
list = [1,2,3,4]
it = iter(list)     #使用inter（）创建迭代器对象
print(next(it))     #使用next（）输出迭代器的下一个元素
print(next(it))
print(next(it))
print(next(it))
#（二）用for语句遍历集合中的元素
list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x,end=" ")

#（三）创建迭代器：在类中构造函数__iter__()与__next__()
class mynumbers:
    def __iter__(self):
      self.a = 1
      return self
    def __next__(self):
      x = self.a
      self.a += 1
      return x

myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#（四）stopiteration:异常结束迭代
class mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
             raise StopIteration
myclass = mynumbers()
myiter = iter(myclass)
for x in myclass:
    print(x)

#切片操作符
t1 = ['java','python','c','c++','js']
t1[0:3]         #从索引0开始索取，直到3为止，但不包括3
print(t1[0:3])  #0可以省略
print(t1[-1])   #[-1]取倒数第一个元素
print(t1[:5:2]) #前5个数每隔2个取一个
print(t1[::2])  #所有数每隔2个取一个



