"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""

"""
x = float(input("x = "))

if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print(f'f({x:.2f}) = {y:.2f}')

"""

"""
Q1:英寸与厘米的转换
A1:
value = float(input("请输入长度："))

unit = input("请输入单位：")

if unit == "in" or unit == "英寸":
    print(f'{value}英寸 = {value * 2.54} 厘米')
elif unit == "cm" or unit == "厘米":
    print(f'{value} 厘米 = {value / 2.54} 英寸')
else:
    print("请输入有效的单位")


"""

"""
Q2
如果输入的成绩在90分以上（含90分）输出A
80分-90分（不含90分）输出B
70分-80分（不含80分）输出C
60分-70分（不含70分）输出D
60分以下输出E。

A2
score = float(input("请输入分数:"))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print("该分数，对应的等级是：", grade)

"""

"""
输入三条边长，如果能构成三角形就计算周长和面积。

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print(f'周长：{a + b + c:.2f}')
    p = (a + b + c) / 2
    area = (p * (p - a)*(p - b)*(p - c)) ** 0.5
    print(f"面积:{area:.2f}")
else:
    print("无法构成三角形")

"""