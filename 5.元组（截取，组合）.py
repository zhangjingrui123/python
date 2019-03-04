#元组（） 与列表类似，不同之处在于元组的元素不能修改,元组使用小括号（）
tup1 = (1,"fibos",3,"baidu",5)
tup2 = (1,)   #只有1个元素的元组，在值后面要加逗号
tup3 = (1,2,3,'fibos',5)
print("tup1[0]: ",tup1[0])
print(tup2)
print("tup3[1:4]: ",tup3[1:4])   #1:4表示从第2个元素开始，截取到第4个元素结束

tup1 = (1,"fibos",3,"baidu",5)
tup2 = (1,2,3,'fibos',5)
tup3 = tup1 + tup2
print(tup3)          #将元组组合到一起
print(tup1[-2])      #反向读取，读取倒数第2个元素


