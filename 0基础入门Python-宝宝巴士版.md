# Python编程从入门到实践

## 第一部分 基础知识

### 第1章 起步

配置Python环境教程（采用conda 创建虚拟环境 防止环境混乱 因为不同的项目需要涉及不同版本的安装包）：

[最新版最详细Anaconda新手安装+配置+环境创建教程_anaconda配置-CSDN博客](https://blog.csdn.net/qq_44000789/article/details/142214660)

VS Code配置Python环境

[10分钟搞定！VS Code配置Python开发环境指南（2025新版） - 知乎](https://zhuanlan.zhihu.com/p/1904849575388361435)

------

可能会出现的问题：

> [!WARNING] 
>
> PS E:\Python编程 从入门到实践> (D:\Anaconda\shell\condabin\conda-hook.ps1) ; (conda activate streamlit) 
>
> >>>>>>>>>>>>>>>>>>>>>> ERROR REPORT <<<<<<<<<<<<<<<<<<<<<< Traceback (most recent call last): File "D:\Anaconda\Lib\site-packages\conda\exception_handler.py", line 16, in __call__ return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "D:\Anaconda\Lib\site-packages\conda\cli\main.py", line 111, in main_sourced print(activator.execute(), end="") UnicodeEncodeError: 'gbk' codec can't encode character '\u202a' in position 410: illegal multibyte sequence

因为系统环境变量被Unicode控制字符污染 可能是之前复制网页中的系统路径时无意中带入

------

成功截图：

![image-20260105110043396](C:\Users\LENOVO\AppData\Roaming\Typora\typora-user-images\image-20260105110043396.png)

第1章总结到此结束！！！😸



### 第2章 变量和简单的数据类型

之后会采用pycharm来进行实例运行 因为用习惯了😂

#### 变量

🦉非常的浅显易懂 

```python
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)
#在程序中，可随时修改变量的值，⽽Python将始终记录变量的最新值
```

![image-20260105112558398](C:\Users\LENOVO\AppData\Roaming\Typora\typora-user-images\image-20260105112558398.png)

message只是一个名字 而赋给它的值定义了它的类型 如果是5那就是整型 如果是""那就是字符串 

Python是动态类型但**强类型语言** 

```python
10 + "a"   # ❌ 直接报错
```

因此Python的变量不是“容器”，而是“标签” => Python用来做AI是非常合适的 因为AI需要随时调参讲究的是一个动态的变化 模型结构本身就是运行期对象，**语言必须允许结构动态变化**

------

> [!TIP]
>
> 变量的命名规范
>
> 1.变量名只能包含字⺟、数字和下划线。变量名能以字母或下划线开头，但不能以数字开头。
>
> 例： message_1✅  1_message❌
>
> 2.变量名不能包含空格
>
> 3.不要将Python关键字和函数名用作变量名 例如：print、input等等
>
> ⚠（剩余是工程上的规范 一是变量名应既简短⼜具有描述性，二是慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0）

------

```python
#2.2.2 使⽤变量时命名错误
message = "Hello Python Crash Course reader!"
print(mesage)
```

![image-20260105134155476](C:\Users\LENOVO\AppData\Roaming\Typora\typora-user-images\image-20260105134155476.png)

> [!CAUTION]
>
> 上面的代码块我只截取了相关的部分 具体的整体章节代码在example文件夹下的2.变量和简单的数据类型.py中
>
> 通过Python解释器提供的报错信息可以发现是代码的第九行 一般变量xxx未定义的报错都是Python无法识别你提供的变量名 **根本在于使用变量前没有给它赋值** 这里的**mesage**可以当作一个**新变量**

#### 字符串

**字符串**（string）就是⼀系列字符。在Python 中，用引号引起的都是字符串（可以是单引号也可以是双引号）
