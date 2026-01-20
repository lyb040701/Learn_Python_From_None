#定义函数
# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")
#
# greet_user()

#向函数传递信息
# def greet_user(username):
#     """显示简单的问候语"""
#     print(f"Hello, {username.title()}!")
#
# greet_user('jesse')

#传递实参
#位置实参
# def describe_pet(animal_type, pet_name):
# 	"""显示宠物的信息"""
# 	print(f"\nI have a {animal_type}.")
# 	print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')

#关键字实参
# def describe_pet(animal_type, pet_name):
# 	"""显示宠物的信息"""
# 	print(f"\nI have a {animal_type}.")
# 	print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')

#默认值
# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet(pet_name='willie')

#等效的函数调用
# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# #一条名为Willie的⼩狗
# describe_pet('willie')
# describe_pet(pet_name='willie')
#
# #一只名为Harry的仓⿏
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

#避免实参错误
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet()

#返回值
#返回简单的值
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

#让实参变为可选的
# def get_formatted_name(first_name, middle_name, last_name):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#
#     return full_name.title()
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

#返回字典
# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person
#
#
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#
#
#     return person
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

#结合使用函数和循环
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

#传递列表
# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

#在函数中修改列表
# # 首先创建一个列表，其中包含一些要打印的设计
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
#
# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

#使用函数实现
# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止打印每个设计后，都将其移到列表completed_models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#
#
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#传递任意数量的实参
# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

#遍历配料列表
# def make_pizza(*toppings):
# 	"""概述要制作的比萨"""
# 	print("\nMaking a pizza with the following toppings:")
# 	for topping in toppings:
# 		print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

#结合使用位置实参和任意数量的实参
# def make_pizza(size, *toppings):
#     """概述要制作的比萨"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#使用任意数量的关键词实参
# def build_profile(first, last, **user_info):
#
# 	"""创建一个字典，其中包含我们知道的有关用户的一切"""
# 	user_info['first_name'] = first
# 	user_info['last_name'] = last
# 	return user_info
#
# user_profile = build_profile('albert', 'einstein',
#                               location='princeton',
#                               field='physics')
# print(user_profile)
