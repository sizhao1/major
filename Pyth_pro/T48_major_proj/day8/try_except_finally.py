'''
python代码中的异常处理:
try...except...: 代码语句块,用于处理异常,不能分割的基础结构.
try:块里面,写可能会出错的代码.  raise: 抛出错误.
except:块里面,处理异常.  一般用Exception来代表所有的错误. (因为Exception类是所有类的父类.)

补充结构:
else: 当try块中不出错的时候,会接着走else块里面的语句内容.
finally: 不管代码有没有出错,都要走到finally,做最后的软件环境处理和资源释放等收尾工作.
'''

try:
    num1 = int(input('请输入一个整数:'))
    num2 = int(input('请再输入一个整数:'))
    if num1>num2:
        print(num1+num2)
    else:
        print(num2/num1)
except Exception as e:
    print('输入的值不对!')
else:
    print('语句都是正确的,没有出错!')
finally:
    print('不管出不出错,都要走到finally!')