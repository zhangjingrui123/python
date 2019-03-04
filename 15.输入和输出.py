#(一)print输出
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')    #结尾加end=' '，表示末尾不换行
    print(repr(x*x*x).rjust(4))                           #rjust()方法可以将字符串靠右，并填充左边空格
for x in range(1,11):
    print('{0:2d} {1:4d} {2:4d}'.format(x,x*x,x*x*x))     #{0:2d}表示第1个参数格式按2个宽度显示，长度不足2用空格补足
                                                          #format（）括号中参数替换前面的（）及里面的字符
print('{name}网址：{site}'.format(name='百度',site='www.baidu.com'))  #使用关键字参数，值会指向使用该名字的参数
#（1）整数输出
print('%o' % 20)                                          #八进制
print('%d' % 20)                                          #十进制
print('%x' % 20)                                          #十六进制
#（2）浮点数输出
print('%f' % 1.11)                                        # 默认保留6位小数：1.110000
print('%.1f' % 1.11)                                      # 取一位小数：1.1
print('%e' % 1.11)                                        # 默认6位小数，用科学计数法：1.110000e+00
print('%.3e' % 1.11)                                      # 默认3位小数，用科学计数法：1.110e+00
print('%g' % 1111.1111)                                   # 默认6位有效数字 :1111.11
print('%.7g' % 1111.1111)                                 # 取7位有效数字:1111.111
print('%.2g' % 1111.1111)                                 # 取2位有效数字，自动转化为科学计数法：1.1e+03 
#（3）字符串输出
print('%s' % 'kello world')                               #字符串输出：hello world
print('%20s' % 'hello world')                             #右对齐，取20位，不够则补位
print('%-20s' % 'hello world')                            #左对齐，取20位，不够则补位
print('%.2s' % 'hello world')                             #取2位：he
print('%10.2s' % 'hello world')                           #右对齐，取2位
print('%-10.2s' % 'hello world')                          #左对齐，取2位he
#（二）input输入，可以接受一个Python表达式作为输入，并将运算结果返回
str = input("请输入：")                                    #input()内置函数从标准输入读入一行文本，默认的标准输入时键盘
print("你输入的内容是：",str)                               
