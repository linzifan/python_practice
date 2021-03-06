## Python 练习册，每天一个小程序 ##

> Credit: 

> 0000 - 0024: [Show-Me-the-Code](https://github.com/Show-Me-the-Code/show-me-the-code)

> 0025: [An Introduction to Interactive Programming in Python (Part 2)](https://class.coursera.org/interactivepython2-002/lecture)

> 0026 - 0033: [Principles of Computing (Part 2)](https://class.coursera.org/principlescomputing2-002/wiki/view?page=practice_recursion)



- [x] **第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

- [x] **第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

- [ ] **第 0002 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

- [ ] **第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。

- [x] **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

- [ ] **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

- [ ] **第 0006 题：**你有一个目录，放了你一个月的日记，都是txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

- [ ] **第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

- [ ] **第 0008 题：**一个HTML文件，找出里面的**正文**。

- [ ] **第 0009 题：**一个HTML文件，找出里面的**链接**。

- [x] **第 0010 题：**使用 Python 生成类似于下图中的**字母验证码图片**

    ![字母验证码](http://i.imgur.com/aVhbegV.jpg)


- [ ] ~~**第 0011 题：**~~ 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

    北京
    程序员
    公务员
    领导
    牛比
    牛逼
    你娘
    你妈
    love
    sex
    jiangge

- [x] **第 0012 题：** 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

- [x] **第 0013 题：** 用 Python 写一个爬图片的程序。


- [x] **第 0014 题：** 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
```
    {
        "1":["张三",150,120,100],
        "2":["李四",90,99,95],
        "3":["王五",60,66,68]
    }
```
请将上述内容写到 student.xls 文件中

- [阅读资料](http://www.cnblogs.com/skynet/archive/2013/05/06/3063245.html) 腾讯游戏开发 XML 和 Excel 内容相互转换

- [x] **第 0015 题：** 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
```
    {
        "1" : "上海",
        "2" : "北京",
        "3" : "成都"
    }
```
请将上述内容写到 city.xls 文件中


- [x] **第 0016 题：** 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
```
    [
        [1, 82, 65535],
        [20, 90, 13],
        [26, 809, 1024]
    ]
```
请将上述内容写到 numbers.xls 文件中

- [ ] **第 0017 题：** 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：
```
    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <students>
    <!--
    	学生信息表
    	"id" : [名字, 数学, 语文, 英文]
    -->
    {
    	"1" : ["张三", 150, 120, 100],
    	"2" : ["李四", 90, 99, 95],
    	"3" : ["王五", 60, 66, 68]
    }
    </students>
    </root>
```

- [ ] **第 0018 题：** 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：
```
    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <citys>
    <!--
    	城市信息
    -->
    {
    	"1" : "上海",
    	"2" : "北京",
    	"3" : "成都"
    }
    </citys>
    </root>
```
- [ ] **第 0019 题：** 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下所示：

```
    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <numbers>
    <!--
    	数字信息
    -->

    [
    	[1, 82, 65535],
    	[20, 90, 13],
    	[26, 809, 1024]
    ]

    </numbers>
    </root>
```
- [ ] **第 0020 题：** [登陆中国联通网上营业厅](http://iservice.10010.com/index_.html) 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。

- [ ] **第 0021 题：** 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

  - 阅读资料 [用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)

  - 阅读资料 [Hashing Strings with Python](http://www.pythoncentral.io/hashing-strings-with-python/)

  - 阅读资料 [Python's safest method to store and retrieve passwords from a database](http://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database)

- [ ] **第 0022 题：** iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。

- [ ] **第 0023 题：** 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

  - 阅读资料[Python 有哪些 Web 框架](http://v2ex.com/t/151643#reply53)

    ![留言簿参考](http://i.imgur.com/VIyCZ0i.jpg)


- [ ] **第 0024 题：** 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

    ![SpringSide 版TodoList](http://i.imgur.com/NEf7zHp.jpg)

- [x] **第 0025 题：** Randomly generate a mapping of cipher. Use it to encode and decode some phrases.

- [x] **第 0026 题：** *Exercises for Recursion* Write a function `triangular_sum(num)` that computes the arithmetic sum 0+1+2...+(num−1)+num. For example, `triangular_sum(3)` should return 6. Note that this sum can be computed directly via a simple arithmetic formula, but use a recursive approach instead.

- [x] **第 0027 题：** *Exercises for Recursion* Write a function `number_of_threes(num)` that returns the number of times the digit 3 appears in the decimal representation of the non-negative integer num. For example `number_of_threes(34534)` should return 2. 

- [x] **第 0028 题：** *Exercises for Recursion* Write a function `is_member(my_list, elem)` that returns True if elem is a member of `my_list` and False otherwise. For example, `is_member(['c', 'a', 't'], 'a')` should return True. Do not use any of Python's built-in list methods or an operator like in. 

- [x] **第 0029 题：** *Exercises for Recursion* Write a function `remove_x(my_string)` that takes the string `my_string` and deletes all occurrences of the character 'x' from this string. For example, `remove_x("catxxdogx")` should return "catdog". You should not use Python's built-in string methods. 

- [x] **第 0030 题：** *Exercises for Recursion* Write a function `insert_x(my_string)` that takes the string `my_string` and adds the character 'x' between each pair of consecutive characters in the string. For example, `insert_x("catdog")` should return "cxaxtxdxoxg". 

- [x] **第 0031 题：** *Exercises for Recursion* Write a function `list_reverse(my_list)` that takes a list and returns a new list whose elements appear in reversed order. For example, `list_reverse([2, 3, 1])` should return [1, 3, 2]. Do not use the reverse() method for lists.

- [x] **第 0032 题：** *Exercises for Recursion* Challenge: Write a function `gcd(num1, num2)` that takes two non-negative integers and computes the greatest common divisor of num1 and num2. To simplify the problem, you may assume that the greatest common divisor of zero and any non-negative integer is the integer itself. For an extra challenge, your programs should only use subtraction. Hint: If you stuck, try searching for "Euclid's Algorithm". 

- [x] **第 0033 题：** *Exercises for Recursion* Challenge: Write a function `slice(my_list, first, last)` that takes as input a list `my_list` and two non-negative integer indices first and last satisfying 0≤first≤last≤n where n is the length of `my_list`. slice should return the corresponding Python list slice `my_list[first:last]`. For example, `slice(['a', 'b', 'c', 'd', 'e'], 2, 4)` should return `['c', 'd']`.
Important: Your solution should not use Python's built-in slice operator `:` anywhere in its implementation. Instead use the method `pop` to remove one element from the input list during each recursion call. 
