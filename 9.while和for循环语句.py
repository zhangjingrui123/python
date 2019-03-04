#循环语句：while和for
#while 循环语句和 for 循环语句使用 else 的区别：
#1、如果 else 语句和 while 循环语句一起使用，则当条件变为 False 时，则执行 else 语句。
#2.如果 else 语句和 for 循环语句一起使用，else 语句块只在 for 循环正常终止时执行！

#（一）计算1-100的总和
#方法一：
n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
print("1 到{}之和为：{}".format(n,sum))   # %d表示为：整数型数值对应的通配符,可以替换成{：}.format()函数
#方法二：                                 # print("1 到 %d 之和为： %d" %(n,sum))
sum = 0
for i in range(1,101):
    sum += i
print(sum)

#（二）while循环语句使用else
count = 0
while count < 5:
    print(count,"小于5")
    count = count +1
else:
    print(count,"大于等于5")

#（三）for 遍历任何序列项目
language = ["java","python","c"]
for c in language:
    print(c)

#（四）break语句，用于跳出当前循环体，终止循环语句
sites = ["baidu","google","taobao"]
for site in sites:
    if site == "taobao":
        print("淘宝")
        break
    print("循环数据" + site)
else:
    print("没有循环数据")
print("完成循环")

#（五）range函数
for i in range(1,10):                              #把1,2,3,4,5,6,7,8,9依次给i赋值（顾头不顾尾）
    for j in range(1,i+1):                         #当i=1.j=(1,2)此时的j赋值就是1
        print('{}*{}={}\t'.format(j,i,i*j),end='') #end=''计算的结尾处加上空格
    print()                                        #format格式化函数，用{}和：代替以前的%
                                                   #\t横向制表符