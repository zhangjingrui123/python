#(一)open 方法用于打开1个文件，并返回文件对象
#open函数常用形式:接受2个参数：文件名和模式open(file,mode='r',encoding='编码格式')
#file:文件路径
#mode:文件打开模式：t/x/b/+/r/r+/rb/rb+/w/w+/wb/wb+/a/a+
'''
t:文本模式
x:写模式
b:二进制模式
+：打开一个文件，可读可写
r: 以只读的方式打开文件
r+:以读写的方式打开
rb:以二进制读的方式打开文件
rb+：以二进制读写的方式打开文件
w:以只写的方式打开文件
w+:以读写的方式打开
wb:以二进制写方式打开
wb+:以二进制读写的方式打开
a:打开一个文件用于追加
a+：打开一个文件用于读写
'''
#(二)文件对象常用函数：
#a.txt文件内容如下：
#www.baidu.com
f = open('c:\a.txt','r')      #打开文件，对文件进行读操作
f.close()                     #关闭文件
print('文件名为: ',f)         
line = f.read(5)              #read：读取文件中指定的字节数，未给定则读取所有内容
print('读取的字符串: %s' % (line))
line = f.readline()           #readline：逐行读取，（）中返回指定大小的字节数
print('读取第一行: %s' % (line))
for index in range(5):
    line = next(f)            #next:返回文件下一行
print('第 %d 行 %s' % (index,line))
f = open('workfile','rb+')
f.write(b'12345678910')
f.seek(5)                     #移动到文件的第5个字节
f.seek(-3,2)                  #移动文件倒数第3个字节,2表示从文件末尾算起
f.seek(1)                     #1表示从文件当前位置算起
#str = 'www.baidu.com'
f.seek(0,2)
line = f.write(str)           #在文件末尾写入一行'www.baidu.com'
for index in range(6):
    line = next(f)            #next:返回文件下一行
    print('输出结果为: %d' % (index,line))



