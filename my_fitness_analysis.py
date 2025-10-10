import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['kaiti']
plt.rcParams['axes.unicode_minus']=False

filepath="D:/OneDrive/Desktop/运动数据模拟.csv"
dataframe=pd.read_csv(filepath)
df=dataframe

print('=====我的运动数据记录=====')
print(df)

print('\n=====基础分析结果=====')
totalminutes=df['时长(分钟)'].sum()
totalcalories=df['消耗卡路里'].sum()

print(f'本周运动总时长={totalminutes}分钟')
print(f'本周总卡路里消耗量={totalcalories}卡')

print('\n各运动类型统计')
sportsummary=df.groupby('运动类型').agg({
    '时长(分钟)':'sum',
    '消耗卡路里':'sum',
    '主观感受评分':'mean'
})
#agg的多种用法
# 1. 对不同的列使用不同的计算
#df.agg({'A': 'sum', 'B': 'mean'})
# 2. 对同一列使用多种计算  
#df['成绩'].agg(['mean', 'max', 'min'])  # 同时计算平均分、最高分、最低分
# 3. 使用自定义函数
#df.agg({'年龄': lambda x: x.max() - x.min()})  # 计算年龄范围

# 常用统计函数家族
#总和 = df['金额'].sum()      # 总和
#平均值 = df['金额'].mean()    # 平均值
#中位数 = df['金额'].median()  # 中位数（不受极端值影响）
#最大值 = df['金额'].max()     # 最大值
#最小值 = df['金额'].min()     # 最小值
#计数 = df['金额'].count()     # 非空值个数
sp=sportsummary
print(sportsummary)

print('n\=====进阶分析=====')
sportsummary['效率']=sp['消耗卡路里']/sp['时长(分钟)']

favorite_sport = sportsummary['主观感受评分'].idxmax()
fa_sport_score = sportsummary['主观感受评分'].max()

most_efficient_sport = sportsummary['效率'].idxmax()
max_efficiency = sportsummary['效率'].max()

print(f'你最喜欢的运动:{favorite_sport}(评分：{fa_sport_score:.1f})')
print(f'效率最高的运动:{most_efficient_sport}(每分钟消耗：{max_efficiency:.1f})卡')

#显示所有运动的效率排名
print('\n运动效率排名:')
efficiency_ranking=sp.sort_values('效率',ascending=False)
pd.set_option('display.float_format', '{:.2f}'.format)#设置显示到两位小数
print(efficiency_ranking[['效率','主观感受评分']])

print("\n正在生成可视化图表...")

# 创建1行2列的子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 图表1：运动时间分布饼图
sportsummary['时长(分钟)'].plot.pie(
    ax=ax1,
    title='运动时间分布',
    startangle=90,
    autopct='%.1f%%'
)
ax1.set_ylabel('')

# 图表2：运动效率柱状图
sportsummary['效率'].plot.bar(
    ax=ax2, 
    title='运动效率对比',
    color='lightcoral'
)
ax2.set_ylabel('卡路里/分钟')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

#:.1f 用于f-string str.format() 较普遍
#%.1f %操作符 用于某些库的特定参数如Matplotlib 更传统
