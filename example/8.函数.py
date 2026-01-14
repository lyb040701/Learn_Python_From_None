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

