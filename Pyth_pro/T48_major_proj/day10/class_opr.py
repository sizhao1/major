'''
类和对象:
类:
三个组成:
类名: 首字母大写,多个单词组成,每个单词的首字母都大写.
属性: 类似于变量的方式书写. name="张三"
方法: 类似于函数的方式书写.
def eat(): pass
类的定义:
class 类名:
    属性名 = 属性值
    def eat(self):
        pass

类的实例化(调用):
对象变量 = 类名()
调用过程:
1.解释器读到类的实例化代码后, 知道要产生一个对象, 在内存中申请一段内存空间来保存这个对象, 此时内存开辟了一段地址空间来保存对象相关的东西.
2.从实例化的地方打上断点, 从断点出发去读取类的定义, 默认读取的是__init__()(构造方法), __init__()的第一个参数是self, 内存自动去赋值,下来按位置传参.
3.挨个执行__init__()里的执行语句, 一般构造方法用来做初始化的,一般会用做给对象赋初值, 类似于: self.XXX = name, 做的操作就是把XXX变量存到对象的内存空间中保存起来.
包括类中的带self参数的方法,都会存到对象的内存空间中
4.构造函数执行完毕,会带对象的内存地址值返回,返回给断点处的对象变量.
所以self的值和对象变量的值一样,都执行对象占用的内存空间.

类属性和对象属性区分:
类属性定义在方法之外,类以内.
对象属性定义在方法里面

类方法和对象方法区分:
类方法上有注解: @classmethod
类方法第一个参数为: cls

对象方法上没有注解
对象方法第一个参数为:self

静态方法上有注解: @staticmethod
静态方法没有预置参数.

面向对象三大特征:
java, ruby
封装:
就是隐藏内部数据和实现细节，仅对外提供公共访问方式。这样子来提高数据和使用的安全性.
比如: java中有四种访问控制: private(类内部使用), default, protected, public(全局使用)
继承:
子承父业:
子类继承父类:  公共属性,公共方法
写法:
class Parent:  #父类
    pass
class Son(Parent):  #子类
    pass

重写: 函数名相同就被认为是同一函数, 如果子类中有和父类中同名的函数,那么子类的函数会覆盖父类的,这个就是重写.
如果需要父类的构造函数, super().__init__()

python支持多继承:

多态: 强数据类型语言中更强调这个概念
支持运行时的数据类型和定义时的数据类型不同.
python天然支持多态,因为python是弱类型数据语言.
'''
# 定义一个人类
class Person:
    # 统计生成的对象数
    count = 0
    def __init__(self,name,age,sex):
        print('我是构造函数中的第一行!')
        print(self)
        self.n = name
        self.a = age
        self.s = sex
        Person.count += 1
    def eat(self):
        print(self.n,'会吃饭!')

    @classmethod
    def print_count(cls):
        print(cls.count)

class Cat:
    count = 0
    def __init__(self,name,type,sex,color):
        self.name = name
        self.type = type
        self.sex = sex
        self.color = color

    def mewing(self):
        print(self.type,self.name,'会喵喵叫!')

class BoSiCat(Cat):
    def __init__(self,name,type,sex,color,age):
        super().__init__(name,type,sex,color)
        self.age = age
    def mewing(self):
        print('波斯猫',self.name,'猫猫叫!')
    def eat(self):
        print(self.name,'喜欢吃鱼')

# b1 = BoSiCat('小波','波斯猫','母','白',4)
# b1.mewing()
# b1.eat()

# print('调用开始!')
# p1 = Person('袁荣兵',22,'男')   #唯一和函数调用有区别的地方,首字母是大写的.
# print(p1)
# p1.eat()
# print(p1.count)
# print(p1.n)
# print(p1.a)
# print(p1.s)
# print('调用结束!')
# p2 = Person('黄菊',22,'女')
# print(p2.count)
# p3 = Person('冯旭阳',22,'男')
# print(p3.count)

# c1 = Cat('小波','波斯猫','母','纯白')
# c1.mewing()

'''
创建一个名为User 的类，其中包含 姓first_name 和名last_name ，还有用户简介通常会存储的其他几个属性(例: 年龄,喜好等)。在类User 中定义一个名为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
'''
class User:
    def __init__(self,first_name,last_name,age=18,like=None):
        self.x=first_name
        self.y=last_name
        self.age=age
        self.like=like
    def describe_user(self):
        print(self.y+self.x,self.age,self.like)
    def greet_user(self):
        print('用户'+self.y+self.x+'你好!')

# u1 = User('小明','张',16,'看电影,听音乐')
# u1.describe_user()
# u1.greet_user()

'''
定义一个学生类。1）有下面的类属性：
1 .姓名2. 年龄3 .成绩（语文，数学，英语)[每课成绩的类型为整数]
2）类方法：
1.获取学生的姓名：get_name() 返回类型:str
2.获取学生的年龄：get_age() 返回类型:int
3.返回3门科目中最高的分数。get_course() 返回类型:int
'''
class Student:
    def __init__(self,name,age,course=[]):
        self._n = name
        self._a = age
        self._c = course
    def _get_name(self):
        return self.n
    def _get_age(self):
        return int(self.a)
    def _get_course(self):
        return max(self.c)

# zm = Student('zhangming',20,[69,88,100])
# zm._a = 29
# print(zm._a)
# print(zm.get_course())

# 定义一个父类
class A:
    def print1(self):
        print('----A----')

# 定义一个父类
class B:
    def print1(self):
        print('----B----')

# 定义一个子类，继承自A、B
class C(A,B):
    pass
    # def printC(self):
    #     print('----C----')

# c = C()
# c.print1()
# print(C.__mro__)

# 看下运行结果
class Parent:        # 定义父类
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")
    def parentMethod(self):
        print('调用父类方法')
    def setAttr(self, attr):
        Parent.parentAttr = attr # Parent.parentAttr = 200
    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)
class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")
    def childMethod(self):
        print('调用子类方法')
# c = Child()      #"调用子类构造方法"
# c.childMethod()  #'调用子类方法'
# c.parentMethod() #'调用父类方法'
# c.setAttr(200)
# c.getAttr()     #"父类属性 :200"

# 看下运行结果
class Parent1:
    def myMethod(self):
        print('调用父类方法1')
class Parent2:
    def myMethod(self):
        print("调用父类方法2")
class Child(Parent2,Parent1):
    def myMethod(self):
        print('调用子类方法')
# c = Child()
# c.myMethod()

'''
2.定义一个学生类,使得可以产生如下对象和使用如下方法:
定义一个父类为学生类,有属性:name, 性别, 有方法: 描述个人信息.
子类有需求如下:
李雷爱跑步，爱吃东西。
韩梅梅光爱跑步,不爱吃东西.
1）李雷体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）韩梅梅的体重是45.0公斤
李雷一天跑步跑三回,吃东西吃五回.
韩梅梅一天跑步跑一回,吃东西只吃一回.
实例化李雷和韩梅梅,调用他们一天跑步和吃东西的方法,打印两人的体重.
'''
class Student:
    def __init__(self,name,sex):
        self.n = name
        self.s = sex
class Junior(Student):
    def __init__(self,name,sex,weight):
        super().__init__(name,sex)
        self.w = weight
    def run(self,num):
        self.w = self.w-0.5*num
    def eat(self,num):
        self.w = self.w+num
# s =Student('李雷','男')
# lilei = Junior('李雷','男',75.0)
# lilei.run(3)
# lilei.eat(5)
# print(f'{lilei.n}的体重为{lilei.w}')
#
# Hmm = Junior('韩梅梅','女',45.0)
# Hmm.run(3)
# Hmm.eat(1)
# print(f'{Hmm.n}的体重为{Hmm.w}')

# java中的函数定义
# public class Ostr(extends Str):
#     pass
# public str add(str o1, str o2){
#     str new_str = o1+o2;
#     return new_str
# }
#
# add(o1,o2)  # 因为java支持多态,所以允许定义时的数据类型和运行时的数据类型不一样,当运行时的数据类型是定义时数据类型的子类时,允许这样使用.
# add('3','5')  #编译的时候,报数据类型错误.

def add(num1=1,num2=2):
    print(num1+num2)

add(3,5)
add(3.5,5.5)
add('3','5')







