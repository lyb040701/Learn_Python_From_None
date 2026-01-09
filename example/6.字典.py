#一个简单的字典
# alien_0 = {'color': 'green', 'points': 5}
#
# print(alien_0['color'])
# print(alien_0['points'])

#使用字典
#访问字典中的值
# alien_0 = {'color': 'green'}
# print(alien_0['color'])
#
# alien_0 = {'color': 'green', 'points': 5}
#
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

#添加键值对
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0 #添加键值对操作
# alien_0['y_position'] = 25 #添加键值对操作
# print(alien_0)

#从创建一个空字典开始
# alien_0 = {} #可以类比于创建一个新列表 list=[] 后面再进行list.append()操作进行添加元素
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
#
# print(alien_0)

#修改字典中的值
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
#
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

#删除键值对
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)

#由类似对象组成的字典
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
#
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

#get()
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)
#
# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points')
# print(point_value)

#遍历字典
#遍历所有的键值对
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
#     }
#
# for key, value in user_0.items():
# 	print(f"\nKey: {key}")
# 	print(f"Value: {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
#
# for name, language in favorite_languages.items():
# 	print(f"{name.title()}'s favorite language is {language.title()}.")

#遍历所有的键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
#
# for name in favorite_languages.keys(): #这里的keys()就不能被替换成其他的了
# 									   #因为这是字典对象的一个属性！
# 	print(name.title())

#按照特定序列遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
#
# for name in sorted(favorite_languages.keys()):
# 	print(f"{name.title()}, thank you for taking the poll.")

#遍历字典中所有的值
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

#集合
# languages = {'python', 'rust', 'python', 'c'}
# print(languages)

#嵌套
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in alie:
#     print(alien)

# 创建一个用于存储外星⼈的空列表

aliens = []

# 创建30个绿色的外星人

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:5]:  # ！！！#遍历列表 索引是默认从0开始的 因此是0 1 2 3 4 左闭右开
#     print(alien)
# print("...")
#
# # 显示创建了多少个外星人
#
# print(f"Total number of aliens: {len(aliens)}")

# favorite_languages = {
#     'jen': ['python', 'rust'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['python', 'haskell'],
# }
#
# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

#在字典中存储字典
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
#
# }
#
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")