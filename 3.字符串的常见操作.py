#find,index,count,replece，split，join,capitalize,splitlines等

#（一）find:检测搜索字符串里的文本/子字符串：beg(开始)和end(结束)索引范围
t1 = "fibos is for you"
print(t1.find("for"))
print(t1.find("for",5))       #搜索指定范围内的字符串，返回开始的索引值
print(t1.find("3"))           #如果不包含字符串，返回-1

#（二）index：和find差不多，但当str不在字符串中的时候会报一个异常
t1 = "fibos is for you"
print(t1.index("for"))
print(t1.index("for",4))         #不包含字符串，报错异常：str not found

#（三）count：统计字符串中某个字符出现的次数
t1 = "fibos is for you"
print(t1.count("s"))  
print(t1.count("s",0,5))        #开始索引到结束索引位置s出现的次数

#（四）replace:将old字符串替换成new字符串
t1 = "fibos is for you"
print("旧名称：",t1)
print("新名称：",t1.replace("fibos","fowallet"))   #replace(旧，新)

#（五）split:通过指定分隔符对字符串进行切片
t1 = "fibos is for you"
print(t1.split())       #以空格为分隔符
print(t1.split('i',1))  #以i为分隔符
print(t1.split('w',))   #以w为分隔符

#（六）join:将指定字符连接成一个新的字符串
t1 = "-"
t2 = ""
str = ("f","i","b","o","s")
print(t1.join(str))
print(t2.join(str))

#（七）capitalize:将字符串的第一个字符转换为大写
t1 = "fibos is for you"
print(t1.capitalize())

#（八）格式化字符串的几种方法：%s,%d,format
t1 = "fibos is %s you" % ("for")  # %s是用来给字符串占位置的
print(t1)                         # %d是用来给数字占位置的

t1 = "fibos is {} you".format("for") #format是用来给{}占位置的
print(t1)               
