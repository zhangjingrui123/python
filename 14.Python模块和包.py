#模块：是包含定义通用的函数，变量和类的文件，后缀名是.py,一个模块就是一个包含Python定义和声明的文件
#（一）引用/导入模块：import / from...import
#（1）将整个模块导入：import somemodule
# (2) 从模块中导入一个函数：from somemodule import 函数
#（3）从模块中导入多个函数：from somemodule import 函数1，函数2，函数3
#（4）将模块的函数全部导入：from somemodule import*
#（5）引用函数时使用别名：  from somemodule as othername
# (6) 多次导入模块。模块只会被加载一次
#（7）内置模块，自定义模块，第三方模块
import sys
print(sys.path)    #sys.path获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下
print(sys.argv)    #sys.argv是一个包含命令行参数的列表
                    
import os          #os处理文件/目录
cmd_res = os.system('dir')
print(cmd_res)
#（二）__name__属性
if __name__ == '__main__':
    print('模块自身在运行')          #__name__属性值是：__mian__时，表明该模块自身在运行
else:
    print('模块被引入')              #import模块被引用

#（三）dir()函数：可以找到模块内定义的所有名称，以一个字符串列表的形式返回
#dir()