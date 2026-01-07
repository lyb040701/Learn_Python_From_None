# 一个简单的示例
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

#条件测试
# car = 'bmw'
# print(car == 'bmw')
#
# car = 'Audi'
# print(car.lower() == 'audi')

# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

#使用and检查多个条件
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)

#if语句
# age = 19
# if age >= 18:
#     print("You are old enough to vote!")
#
#
# age = 17
# if age >= 18:
#       print("You are old enough to vote!")
#       print("Have you registered to vote yet?")
# else:
# 	print("Sorry, you are too young to vote.")
# 	print("Please register to vote as soon as you turn 18!")
#
# age = 12
# if age < 4:
# 	print("Your admission cost is $0.")
# elif age < 18:
# 	print("Your admission cost is $25.")
# else:
# 	print("Your admission cost is $40.")

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
# 	print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
# 	print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
# 	print("Adding extra cheese.")
# print("\nFinished making your pizza!")
#
# requested_toppings = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_toppings:
# 	print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
# 	print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
# 	print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")
#
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
# 	if requested_topping == 'green peppers':
# 		print("Sorry, we are out of green peppers right now.")
# 	else:
# 		print(f"Adding {requested_topping}.")
#
# print("\nFinished making your pizza!")
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")
#
# available_toppings = ['mushrooms', 'olives', 'green peppers',
# 					  'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
# 	if requested_topping in available_toppings:
# 		print(f"Adding {requested_topping}.")
# else:
# 	print(f"Sorry, we don't have {requested_topping}.")
#
# print("\nFinished making your pizza!")

# is_admin = True
#
# if(is_admin or print("显示管理员面板")==None):
#     print(1)

# is_admin = False
# if(is_admin and print("显示管理员面板")==None):
#     print(1)