# 遍历整个列表
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# 在for循环中执行更多的操作
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# 	print(f"{magician.title()}, that was a great trick!")

# 1.忘记缩进
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)

# 2.不必要的缩进
# message = "Hello Python world!"
#     print(message)

# 3.遗漏冒号
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians
# 	print(magician)

# range()函数
# for value in range(1, 5):
#     print(value)

# 使用range()创建数值列表
# numbers = list(range(1, 6))
# print(numbers)

# 在使用range()函数时，还可指定步长 给这个函数指定第三个参数，Python将根据这个步长来生成数
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#      square = value ** 2
#      squares.append(square)
# print(squares)

# 对数值列表执行简单的统计计算
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# 切片
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# 输出：['charles', 'martina', 'michael']

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[1:4])
# 输出：['martina', 'michael', 'florence']

# 如果没有指定第一个索引，自动从列表开头开始
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[:4])
# 输出：['charles', 'martina', 'michael', 'florence']

# 要让切片终⽌于列表末尾，也可使用类似的语法
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[2:])
# 输出：['michael', 'florence', 'eli']

# 负数索引返回与列表末尾有相应距离的元素，因此可以输出列表末尾的任意切片
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])

# 复制列表
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
#
# print("My favorite foods are:")
# print(my_foods)
#
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# 容易犯的误区
# my_foods = ['pizza', 'falafel', 'carrot cake']

# 这是行不通的：
# friend_foods = my_foods
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# 小小测试
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# n = len(players)
#
# print(players[int((n - 1) / 2) - 1:int((n - 1) / 2) + 2])

#元组
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

#修改元组
# dimensions = (200, 50)
# dimensions[0] = 250

#单个元素的元组
# my_t = (3)
# for item in my_t:
#     print(item)

# my_t = (3,)
# for item in my_t:
#     print(item)
# print(type(my_t))