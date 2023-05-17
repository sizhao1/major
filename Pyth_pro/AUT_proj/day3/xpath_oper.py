'''
xpath定位:
xml文件路径的定位方法.

1.绝对路径定位
以./开始,从根节点出发,每经过一个层级就用一个/表示.
例:/html/body/form/div/fieldset/p[1]/input[1]

2.相对路径定位
以//开始,从任意节点出发,每经过一个层级就用一个/表示,如果需要跳层级,可以用//表示.
//后一定要跟标签,如果知道确切的标签,直接写标签名, 如果不知道, //*表示匹配任意标签.

a.结合标签名查找   例: //div
b.结合属性查找     例://*[@属性名=属性值]
c.结合逻辑运算符查找
and: 逻辑与运算  前面一个属性也得符合,后面一个也得符合.
例: //input[@name="user" and @class="login"]
or: 逻辑或运算   前面一个符合也行,后面一个符合也行.
例: //input[@name="user" or @class="login"]
not: 逻辑非运算  对not后的表达式进行取反操作. tips:一定带个(),先运算()里面的,再对结果取反.
//input[not (@name="user" or @class="login")]
d. 结合层级查找
//*[@id="p1"]/input[1]
//*[@id="p1"]//input

延伸:
1.文本类标签的定位
//*[text()="文本内容"]: *不限制标签,只要这个标签它的文本和文本内容一致,这个标签就会被返回.
2.匹配以什么开头的一段属性值
//*[starts-with(@属性名,'开头的一段属性值')]
3.匹配包含的一段属性值
//*[contains(@属性名,'包含的一段属性值')]

补充:
序数的写法:  同个层级下,论的是标签,标签[n]表示在同个层级下,同样的标签,这个是第几个标签.
'''
from selenium import webdriver
from day1.basic import *
import time

def test_goods_detail(color,memory,tc):
    print(dr.title)
    # 选择商品属性
    dr.find_element_by_xpath(f'//*[@data-value="{color}"]').click()
    dr.find_element_by_xpath(f'//*[@data-value="{memory}"]').click()
    dr.find_element_by_xpath(f'//*[@data-value="{tc}"]').click()
    # 打印商品价格
    print(dr.find_element_by_xpath('//*[@id="data_shopPrice"]').text)
    # 增加一个数量
    dr.find_element_by_xpath('//*[text()="+"]').click()
    # 加入购物车
    dr.find_element_by_xpath('//*[@id=\'joinCarButton\']').click()
    time.sleep(3)

def test_page_detail(dr,title):
    dr.find_element_by_xpath(f'//*[text()="{title}"]').click()
    # 切换窗口
    dr.switch_to.window(dr.window_handles[-1])
    # 打印导航信息
    print(dr.find_element_by_xpath('//*[@class="Nowposition w1100"]/div').text)
    # 打印文章标题
    print(dr.find_element_by_xpath('//*[@class="Title-article"]/p').text)
    # 打印文章内容
    print(dr.find_element_by_xpath('//*[@class="article-body"]').text)
    # 打印上一篇文章
    print(dr.find_element_by_xpath('//*[@class="othe-consult"]//a').text)
    # 打印右侧的热门资讯
    print(dr.find_element_by_xpath('//*[@class="consult-R fr"]').text)

if __name__ == '__main__':
    url = 'http://127.0.0.1:85'
    # 测试预置条件
    dr = pre_test(url)
    # 执行步骤
    test_page_detail(dr,'有商品上架咯...')
    # 结束测试
    end_test(dr)