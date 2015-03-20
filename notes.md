## Notes on Python

1. What does `if __name__ == "__main__":` do?

When the Python interpreter reads a source file, it executes all of the code found in it. Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special `__name__` variable to have a value `"__main__"`. If this file is being imported from another module, `__name__` will be set to the module's name.

2. Encoding

[字符编码详解](http://www.crifan.com/files/doc/docbook/char_encoding/release/html/char_encoding.html)
