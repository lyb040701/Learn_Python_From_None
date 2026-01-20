# 创建和使用类
# class Dog:
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟⼩狗收到命令时坐下"""
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         """模拟⼩狗收到命令时打滚"""
#         print(f"{self.name} rolled over!")

# 根据类创建实例
# my_dog = Dog('Willie', 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")

# 调用方法
# class Dog:
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟⼩狗收到命令时坐下"""
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         """模拟⼩狗收到命令时打滚"""
#         print(f"{self.name} rolled over!")
#
#
# my_dog = Dog('Willie', 6)
# my_dog.sit()
# my_dog.roll_over()

# 创建多个实例
# class Dog:
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟⼩狗收到命令时坐下"""
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         """模拟⼩狗收到命令时打滚"""
#         print(f"{self.name} rolled over!")
#
#
# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)
#
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
#
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()

# 使用类和实例
# class Car:
#     """一次模拟汽车的简单尝试"""
#     def __init__(self, make, model, year):
#         """初始化描述汽⻋的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_descriptive_name(self):
#         """返回格式规范的描述性信息"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# 继承
# class Car:
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0
#
# 	def get_descriptive_name(self):
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()
#
# 	def read_odometer(self):
# 		print(f"This car has {self.odometer_reading} miles on it.")
#
# 	def update_odometer(self, mileage):
# 		if mileage >= self.odometer_reading:
# 			self.odometer_reading = mileage
# 		else:
# 			print("You can't roll back an odometer!")
#
# 	def increment_odometer(self, miles):
# 		self.odometer_reading += miles
#
# class ElectricCar(Car):
# 	def __init__(self, make, model, year):
# 		super().__init__(make, model, year)
#
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# 给子类定义属性和方法
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#
#         else:
#             print("You can't roll back an odometer!")
#
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 40
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()

#重写父类中的方法
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#
#         else:
#             print("You can't roll back an odometer!")
#
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#     def fill_gas_tank(self):
#         print("This car has a gas tank!")
#
#
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 40
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#     def fill_gas_tank(self):
#         print("This car doesn't have a gas tank!")
#
# my_used_car = Car('subaru', 'outback', 2019)
# my_used_car.fill_gas_tank()
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# my_leaf.fill_gas_tank()


#将实例用作属性
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery:
#     def __init__(self, battery_size=40):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()

#在一个模块中导入另一个模块
from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())