# Text1
# 使用一个for循环打印数1~20（含）
# for i in range(1,21):
#     print(i)

#Text2
#创建⼀个包含数1~1000000的列表，再使用一个for循环将这些数打印出来。（如果输出的时间太长，按 Ctrl+C停止输出，或关闭输出窗口。）
# numbers = list(range(1,1000001))
# for num in numbers:
#     print(num)

# Text3
# 创建一个包含数1~1000000的列表，再使用min()和max()核实该列表确实是从1开始、到1000000结束的。另外，对这个列表调用函数 sum()，看看Python将100万个数相加需要多长时间。
# listnumber = list(range(1,1000001))
# print(min(listnumber))
# print(max(listnumber))
# print(sum(listnumber))

# Text4
# 通过给range()函数指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for循环将这些数打印出来。
# Odd_number = list(range(1,21,2))
# for num in Odd_number:
#     print(num)

# Text5
# 创建⼀个列表，其中包含3~30内能被3整除的数，再使用一个for循环将这个列表中的数打印出来。
# div_numbers = list(range(3,31,3))
# for num in div_numbers:
#     print(num)


# Text6
# 将同一个数乘三次称为立方。例如，在Python中， 2 的立方用 2**3 表示。创建一个列表，其中包含前10个整数（1~10）的立方，再使用一个for循环将这些立方数打印出来。
# cube_numbers = []
# for i in range(1,11):
#     cube_numbers.append(i**3)
#
# for num in cube_numbers:
#     print(num)

# Text7
# 使用列表推导式生成一个列表，其中包含前10个整数的立方。
# cube_numbers = [value**3 for value in range(1,11)]
# for num in cube_numbers:
#     print(num)

#猜数字游戏
# import random
# number = random.randint(1, 100)
# Flag = True
# while Flag:
#     your_number = int(input("请输入你的数字:"))
#     if your_number == number:
#         Flag = False
#         break
#     elif your_number > number:
#         print("太大了嗷!")
#     else:
#         print("太小了嗷!")
# print("恭喜你猜对了!")