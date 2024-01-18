"""
Q1:
华氏温度转换为摄氏温度。

hint:华氏温度到摄氏温度的转换公式为：$C=(F - 32) /div 1.8$
"""


'''
A1
f = float(input("请输入华氏温度："))

c = (f - 32)/1.8

print("%.1f 华氏度 = %.1f 摄氏度" % (f, c))

print(f'{f:.1f} 华氏度 = {c:.1f} 摄氏度')

'''

'''
Q2
输入半径计算圆的周长和面积

'''


'''
A2
radius = float(input("请输入圆的半径："))

perimeter = radius * 3.1416 * 2
area = radius * radius * 3.1416

print(f'周长：{perimeter:.3f}')
print(f'面积：{area:.3f}')

'''


'''
Q3
输入年份判断是否是闰年

'''

'''
A3
year = int(input("请输入年份："))

is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_leap)

'''