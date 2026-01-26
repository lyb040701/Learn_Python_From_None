# 读取文件
# from pathlib import Path
#
# path = Path('for_you.txt')
# contents = path.read_text()
# print(contents)

# 访问文件中的各行
# from pathlib import Path
#
# path = Path('for_you.txt')
# contents = path.read_text()
#
# lines = contents.splitlines()
# for line in lines:
#     print(line)

# 使用文件的内容
# from pathlib import Path
#
# path = Path('for_you.txt')
# contents = path.read_text()
#
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line
#
# print(pi_string)
# print(len(pi_string))

# from pathlib import Path
#
# path = Path('for_you.txt')
# contents = path.read_text()
#
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
#
# print(pi_string)
# print(len(pi_string))

# 包含100万位的大型文件
# from pathlib import Path
#
# path = Path('pi_million_digits.txt')
# contents = path.read_text()
#
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
#
# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# 圆周率里包含你的生日吗
# from pathlib import Path
#
# path = Path('pi_million_digits.txt')
# contents = path.read_text()
#
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
#
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# 写入文件
# 写入一行
# from pathlib import Path
#
# path = Path('programming.txt')
# path.write_text("I love you!")

# 写入多行
# from pathlib import Path
#
# contents = "I love you!\n"
# contents += "You are like diamonds in the sky!\n"
# contents += "Your beauty leaves me speechless.\n"
#
# path = Path('programming.txt')
# path.write_text(contents)

# 异常
# print(5/0)

# 使用try-except模块
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# 使用异常避免奔溃
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#
#     if second_number == 'q':
#         break
#
#     answer = int(first_number) / int(second_number)
#     print(answer)

# else代码块
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#
#     if second_number == 'q':
#         break
#
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# 处理FileNotFoundError异常
# from pathlib import Path
#
# path = Path('alice.txt')
# contents = path.read_text(encoding='utf-8')

# from pathlib import Path
# path = Path('alice.txt')
# try:
# 	contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
# 	print(f"Sorry, the file {path} does not exist.")


# 存储数据
# 使用json.dumps()和json.loads()
# from pathlib import Path
# import json
#
# numbers = [2, 3, 5, 7, 11, 13]
# path = Path('numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)

# from pathlib import Path
# import json
# path = Path('numbers.json')
# contents = path.read_text()
# numbers = json.loads(contents)
# print(numbers)

# 保存和读取用户生成的数据
# from pathlib import Path
# import json
# username = input("What is your name? ")
# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)
# print(f"We'll remember you when you come back, {username}!")

# from pathlib import Path
# import json
#
# path = Path('username.json')
# contents = path.read_text()
# username = json.loads(contents)
# print(f"Welcome back, {username}!")

# from pathlib import Path
# import json
#
# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")

# 重构
# from pathlib import Path
# import json
#
#
# def greet_user():
#     path = Path('username.json')
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")
#
#
# greet_user()

# from pathlib import Path
# import json
#
#
# def get_stored_username(path):
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None
#
#
# def greet_user():
#     path = Path('username.json')
#     username = get_stored_username(path)
#
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")
# greet_user()

# from pathlib import Path
# import json
#
#
# def get_stored_username(path):
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None
#
# 
# def get_new_username(path):
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     return username
#
#
# def greet_user():
#     path = Path('username.json')
#     username = get_stored_username(path)
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = get_new_username(path)
#         print(f"We'll remember you when you come back, {username}!")
#
#
# greet_user()
