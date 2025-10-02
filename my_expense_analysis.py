import pandas as pd
import matplotlib.pyplot as plt

#第一步：创建数据 - 模拟你一周的消费记录
#我们将创建一个Python字典来表示数据
data = {
    '日期':['周一','周二','周三','周四','周五','周六','周日'],
    '类别':['饮食','交通','饮食','学习','娱乐','购物','饮食'],
    '金额':[25,8,30,50,100,150,40]
}
#第二步：创建一个 DataFrame
df = pd.DataFrame(data)

#打印整个表格，查看数据
print('==== 我的原始消费记录 ====')
print(df)

#第三步：进行简单的数据分析
print('\n==== 数据分析结果 ====')
#计算总支出
total_spending = df['金额'].sum()
print(f'本周总支出：{total_spending}元')

#计算各类别花费
category_spending = df.groupby('类别')['金额'].sum()
print('\n分类别支出')
print(category_spending)

#第四步：数据可视化 - 画出饼图
#让数据说话，直观看到钱花在哪里
print('n\正在生成图表...')
category_spending.plot.pie(
    title='本周消费比例分布',
    autopct='%1.1f%%',#显示百分比
    startangle=90 #让饼图从正上方开始
)
plt.ylabel('') #隐藏y轴标签
plt.show()
