# 2.2变量
# message = "Hello Python world!"
# print(message)
# message = "Hello Python Crash Course world!"
# print(message)

# 2.2.2 使⽤变量时命名错误
# message = "Hello Python Crash Course reader!"
# print(mesage)

# 2.3字符串
# message = "The language \"Python\" is named after Monty Python, not the snake."
# print(message)

# text = '''老师说："今天的作业主题是'Python 的字符串处理'，请大家认真完成，并在作业中写明：'我已经理解了双引号"和单引号'的区别'。" '''
# print(text)

# title()
# name = "tian lin ying"
# print(name.title())

# upper()/lower()
# name = "Tian Lin Ying"
# print(name.upper())
# print(name.lower())

#在字符串中使用变量
# first_name = "lin ying"
# last_name = "tian"
# fullname = f"{first_name} {last_name}"
# print(fullname)
# print(f"Hello, {fullname.title()}!")

#使用f字符串来创建消息
# first_name = "lin ying"
# last_name = "tian"
# fullname = f"{first_name} {last_name}"
# message = f"Hello, {fullname.title()}!"
# print(message)

#使用制表符或换行符来添加空白
# print("Python")
# print("\tPython")
# print("Languages:\nPython\nC\nJavaScript")
# print("Languages:\n\tPython\n\tC\n\tJavaScript")

#rstrip() 删除字符串右端空白
# favorite_language = ' python '
# print(favorite_language.rstrip())

#lstrip() 删除字符串左端空白
# favorite_language = ' python '
# print(favorite_language.lstrip())

#removeprefix() 删除前缀
# nostarch_url = 'https://nostarch.com'
# simple_url = nostarch_url.removeprefix('https://')
# print(simple_url)

#removesuffix() 删除后缀
# filename = "python_notes.txt"
# print(filename.removesuffix('.txt'))

#数
print(0.2 + 0.1)
universe_age = 14_000_000_000
print(universe_age)