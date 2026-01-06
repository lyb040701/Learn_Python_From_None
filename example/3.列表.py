#列表的定义
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

#访问列表元素
# bicycles = ['trek', 'cannondale', 'redline', 'specialized', 1]
# print(bicycles[4])

#索引
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[1])
# print(bicycles[3])

#特殊语法
# print(bicycles[-1])

#使用列表中的各个值
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f"My first bicycle was a {bicycles[0].title()}."
# print(message)

#修改列表元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

#在列表末尾添加元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)

#append()方法让动态地创建列表易如反掌
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

#使⽤del语句删除元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)

#使⽤pop()方法删除元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles.pop()
# print(motorcycles)

#使⽤pop()删除列表中任意位置的元素，只需要在括号中指定要删除的元素的索引即可
# motorcycles = ['honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

#remove()
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

#sort()排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
#
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True) #与字母顺序相反的顺序排列列表元素
# print(cars)

#使用sorted()函数对列表进行临时排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)

#反向打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)