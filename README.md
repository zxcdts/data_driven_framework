# data_driven_framework
## 目录结构
#### 1 Util包：封装常用的函数和功能
    Excel
    时间
    取元素
    写日志
    mapojbect 程序
    解析ini文件
    可选：截屏、建目录、文件操作
#### 2 工程变量包
    通用的所有通用的变量或者配置相关的变量都存在这里
#### 3 PageObject 包
    一个页面一个类，里面很多的方法，方法是用于获取页面中的一个元素
    login类：
    写一个方法叫做get_frame,可以获取到frame对象
    写一个方法叫做get_username,可以获取到username的输入框
    写一个方法叫做get_password,可以获取到password的输入框
    。。。。。。。
    element 对象
#### 4 conf配置目录：
    所有的配置文件：
    日志的配置文件
    定位元素的表示配置文件
#### 5 Action包
    login 函数：所有登录的脚本逻辑
    addContact：添加联系人的脚本逻辑
#### 6 可选的（截屏目录）
    出错的截图
#### 备注
    1. login_info文件中的邮箱与密码是在测试代码时使用，请自行修改
    2. 实际测试过程中的Excel表格中的密码也请自行修改