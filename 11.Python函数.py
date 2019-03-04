#（一）定义函数：def 函数名（参数）：函数体
def area(width,height):         #定义函数时，小括号中的参数，是用来接收参数用的，在函数内部作为变量使用（形参）
    return width * height                  
w = 4
h = 5
print("width =",w,"height =",h,"area =",area(w,h))

#（二）调用函数：函数的基本结构完成以后，通过另一个函数调用执行
def printme(str):               #调用函数时，小括号中的参数，是用来把数据传递到函数内部用的（实参）
    print(str)
    return             
printme("调用用户自定义函数")

#（三）函数返回值:返回函数的处理结果（return）
def fun():
    b = [1,2,3]
    return b                   #可以是任何数据类型（有返回值）
ret = fun()                    #保存函数的返回值，直接使用
print(ret)                     #return关键字：有返回值用变量接受，没有默认返回none
#（四）4种函数类型：
#（1）无参数无返回值：
def printmenu():               #无参数
    print("python")            #无返回值
printmenu()                    
#（2）无参数有返回值：
def languages():               #无参数
    return "python"            #有返回值
language = languages()
print("语言：",language)
#（3）有参数无返回值：          
def languages(str):            #有参数
    str = "java"               #无返回值
print() 
#（4）有参数有返回值：
def area(width,height):        #有参数
    return width * height      #有返回值            
w = 4
h = 5
print("width =",w,"height =",h,"area =",area(w,h))

#（五）函数的嵌套调用：
def testB():
    print("B开始")         
    print("B结束")
def testA():                  #函数A调用函数B，先把函数B中的任务都执行完毕之后再回到函数A继续执行
    print("A开始")
    testB()
    print("A结束")
testA()

#（六）匿名函数：使用lambda来创建匿名函数（不再使用def这样的标准语句定义函数）
sum = lambda t1,t2: t1+t2
print("和等于：",sum(10,20))






