#面向对象：创建一个对象，在对象内部封装多个不同的方法，让不同的对象调用不同的方法
#类的定义：拥有相同属性和方法的对象的集合
#类的作用：属性引用和实例化
#属性：类创建出来的对象特征
#方法：类创建出来的对象技能（定义在类中的函数）
#对象：类的实例化，类是抽象的概念，对象是实实在在存在的东西
#面向对象的3大特征：封装，继承，多态
#封装：将对象的属性和行为（方法）封装起来（对外部不可见）
#继承：子类继承父类，父类的属性和行为子类也都有，并且子类有特有的属性和方法（扩展类的功能）
#多态：同一种方法在子类和父类间有不同的用法（方法的重载，对象的多态）
#方法重写：父类方法的功能不能满足需求，可以在子类中重写父类的方法
class person():                         #这是一个person类
    def __init__(self,name,age):      #为实例对象进行数据初始化
        self.name = name              #name,age为对象的属性
        self.age = age
object1 = person('张三','18')     #创建实例对象,person()构造器
print(object1.name)
print(object1.age)

class people:
    name = ''                      #定义基本属性
    age = 0            
    __weight = 0                   #定义私有属性
    def __init__(self,n,a,w):      #定义构造方法
        self.name = n
        self.age = a
        self.__weigth = w
    def speak(self):
        print('%s 说：我 %d 岁。' %(self.name,self.age))
#单继承
class student(people):
    grade = ''
    def __init__(self,n,a,g):
        people.__init__(self,n,a,g)     #调用父类的构造函数
        self.grade = g
    def speak(self):                    #覆写父类的方法
        print('%s 说：我 %d 岁 了，我在上 %d 年级' %(self.name,self.age,self.grade))

#多继承
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我叫 %s，我是第一个演说家，我演讲的主题是 %s' %(self.name,self.topic))
class smaple(speaker,student):
    a =''
    def __init__(self,n,a,g,t):
        student.__init__(self,n,a,g)
        speaker.__init__(self,n,t)

test = smaple('jack',10,3,'python')           #实例化类
test.speak()
#方法重写
class parent:             #定义父类
    def mymethod(self):
        print('调用父类方法')
class child(parent):      #定义子类
    def mymethod(self):
        print('调用子类方法')

c = child()               #子类实例
c.mymethod()              #子类调用重写方法
super(child,c).mymethod() #用子类对象调用父类已被覆盖的方法
    






