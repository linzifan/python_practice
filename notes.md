## Notes on Python

- What does `if __name__ == "__main__":` do?

When the Python interpreter reads a source file, it executes all of the code found in it. Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special `__name__` variable to have a value `"__main__"`. If this file is being imported from another module, `__name__` will be set to the module's name.

- Encoding

    [字符编码详解](http://www.crifan.com/files/doc/docbook/char_encoding/release/html/char_encoding.html)
    
    [字符编码笔记：ASCII，Unicode和UTF-8 - 阮一峰](http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html)

- [Python简史](http://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html)

- [Linux的概念和体系 - Vamei](http://www.cnblogs.com/vamei/archive/2012/10/10/2718229.html)

- [Python快速教程 - Vamei](http://www.cnblogs.com/vamei/archive/2012/09/13/2682778.html)

- 标准库(standard library) 
  1. 文字处理：`re`, `string`, `textwrap`
  2. 日期和时间：`time`, `datetime`
  3. 数学运算：`numpy`

- [Free Blog with Github Pages](http://dylanninin.com/blog/2013/11/02/free_blogs.html)
