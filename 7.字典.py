#字典{}                     #无序的键值对集合，同一字典内的键必须是互不相同的：{key:value}
dict = {'taobao':'马云','baidu':'yun','aliababa':'老马','tengxun':'马化腾'}
print(dict['baidu'])        #访问字典中的键值

dict = {'taobao':'马云','baidu':'yun','aliababa':'老马','tengxun':'马化腾'}
dict['fibos'] = 'xiangma'    #创建键值对
dict['fibos'] = '响马'       #修改键值对
del dict['aliababa']        #删除键值对
print(dict)

dict = {'taobao':'马云','阿里巴巴':'老马','tengxun':'马化腾'}
print(dict)                #不能用列表作为键，如果同一个键赋值2次，后一个值被记住
'fibos' in dict           #查询指定键是否存在于字典

dict = {'taobao':'马云','阿里巴巴':'老马','tengxun':'马化腾'}
len(dict)                   #计算键的总数
print(len(dict))             

dict = {'taobao':'马云','阿里巴巴':'老马','tengxun':'马化腾'}
type(dict)                 #返回输入的变量类型
print(type(dict))

dict = {'taobao':'马云','阿里巴巴':'老马','tengxun':'马化腾'}
for x,y in dict.items():    #遍历字典中的键值
    print("{},{}".format(x,y))

dict = {'taobao':'马云','阿里巴巴':'老马','tengxun':'马化腾'}
dict.setdefault('fibos','响马')    #如果键不存在于字典中，将会添加键并设为默认值（default）
print(dict)







