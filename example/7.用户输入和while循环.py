#用户输入和while循环

#input()
# age = input("How old are you?")
# print(age>=18)

#int()类型转换
# age = input("How old are you?")
# #模拟终端输入 <<<How old are you?21
# age = int(age)
# print(age>=18)


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

#通过使用标志可以让上述程序更为简洁易懂
# active = True
# while active:
# 	message = input()
# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)