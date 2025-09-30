# 第一部分：if条件判断 - 让程序根据时间打招呼
#===================================================

#导入时间获取模块
import datetime

#获取当前小时数
current_time = datetime.datetime.now().hour

#根据当前小时数，判断是上午下午还是晚上
if current_time < 12:
    greeting = "上午好"
elif 12 <= current_time <18:
    greeting='中午好'
else:
    greeting='晚上好'

#打印带有时间问候的标题
print(f'{greeting}! 这是我的个人信息卡')
print('=' * 40)

#第二部分：for 循环 - 让程序自动列出所有爱好
#===================================================

#原始信息
my_name = '叶培昊'
my_major = '大数据管理与应用'

#创建一个列表（list）来存储多个爱好
my_hobbies = ['听音乐','打羽毛球','学习编程','看电影']
#列表就像一个储物架，可以按顺序放很多东西

print('姓名', my_name)
print('专业', my_major)

#使用 for 循环来遍历并打印每一个爱好
print('我的爱好有')
# 对于hobbies 列表里的‘每一个’爱好，都执行以下操作
for hobby in my_hobbies:
    #这行代码会被重复执行，每次打印一个爱好
    print(f' - {hobby}')

print('='*40)
print('看，我的程序变得‘智能’又‘勤奋’了')
