#（一）调用函数时可传递的参数类型：（默认参数，必需参数，关键字参数，可变参数）
#（1）默认参数：函数调用时，如果没有传递参数，则会使用默认参数
def stu_register(name,age,course,country="CN"):   #默认定义的参数名要放在没有定义的参数名后面
	print("----注册学生信息----")
	print("姓名：",name)
	print("年龄：",age)
	print("课程：",course)
	print("国籍：",country)
stu_register("张三",20,"linux","CN")
stu_register("李四",21,"mysql")
stu_register("王五",22,"python")
#（2）必需（位置）参数：以正确的顺序传入参数，调用时的数量必须和声明时的一样
def stu_register(name,age,course,country): 
	print("----注册学生信息----")
	print("姓名：",name)
	print("年龄：",age)
	print("课程：",course)
	print("国籍：",country)
stu_register("张三",20,"linux","CN")      #调用函数数量必须与定义的函数顺序一致
stu_register("李四",21,"mysql","EN")
stu_register("王五",22,"python","CN")
#（3）关键字参数：不想按顺序传动参数时，只需指定参数名即可，但关键参数必须放在位置参数之后
def stu_register(name,age,course,country="CN"):
	print("----注册学生信息----")
	print("姓名：",name)
	print("年龄：",age)
	print("课程：",course)
	print("国籍：",country)
stu_register(age=22,name="张三",course="linux")
#（4）可变参数（不定长参数）：定义函数时，不命名参数名(*args和**kwargs)
def stu_register(name,age,*args):         #*args会把多传入的参数变成一个元组（）形式输出
	print(name,age,args)
stu_register("张三",21,"CN","python")     #输出：（'CN','python'）
stu_register("李四",22)                   #输出：李四 22（）：（）就是args，只是因为没传值，所以为空]

def stu_register(name,age,*args,**kwargs):      #**kwargs会把多传入的参数变成一个字典{}形式输出
	print(name,age,args,kwargs)
stu_register("李四",20)                         #输出：李四 20 （）{}：{}就是{}，没有传值所以为空
stu_register("张三",21,"CN","python",sex="male")#输出：张三 21 ('CN'，'python') {'sex':male}

#（二）全局变量和局部变量
#局部变量：函数内部定义的变量
#全局变量：既能在一个函数中使用，也能在其他函数中使用
total = 0                       #total在这里是全局变量
def sum(a,b):                   #返回2个参数的和
	total = a + b               #total在这里是局部变量
	print("函数内是局部变量：",total) 
	return total
#调用sum函数
sum(10,20)
print("函数外是全局变量：",total)
#(三)global和nonlocal
num = 1
def fun1():
	global num         #使用global关键字，将函数内的局部变量修改为全局变量
	print(num)         #修改前
	num = 123          #修改后
	print(num)
fun1()
print(num)

def outer():
	num = 10
	def inner():
		nonlocal num   #nonlocal关键字，告诉解释器当前变量不是局部变量
		num = 100
		print(num)
	inner()
	print(num)
outer()
