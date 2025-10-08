import pandas as pd
import matplotlib.pyplot as plt

# === 中文显示配置 ===
plt.rcParams['font.sans-serif'] = ['SimHei','Microsoft YaHei','KaiTi']#常用中文字体
plt.rcParams['axes.unicode_minus'] = False #解决负号显示问题

#文件路径
#下面的路径需要替换为你电脑上的实际路径
#获取方法：右键点击csv文件->属性->查看位置信息

#第一步：从csv文件中读取数据
file_path = 'D:/OneDrive/Desktop/my_real_expense.csv'
df = pd.read_csv(file_path)

#第二步：显示读取的数据
print('==== 从文件读取的消费记录 ====')
print(df)

#第三步：数据分析
print('\n==== 数据分析结果 ====')
total_spending = df['金额'].sum()
print(f'本周总支出：{total_spending}元')

category_spending = df.groupby('类别')['金额'].sum()
print('\n分类别支出：')
print(category_spending)

#第四步：可视化
print('\n正在生成图表...')
category_spending.plot.pie(# .plot.pie 用于制饼图
    title='本周消费比例分布',
    autopct='%d%%',#d保留整数位 .n保留n位小数 对象都是图表各数据的比例
    #前一个%表示格式说明的开始 后两个%%表示输出一个%
    startangle=90
)
plt.ylabel('')#括号内用于y轴标签，空格则y轴无内容
plt.show()#此行用于显示饼图，相当于print的作用
