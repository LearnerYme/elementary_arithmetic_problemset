# elementary_arithmetic_problemset
你可以使用这个小学生算术题生成器来自动产生很多道给小学生做的加减乘除题目。比如给你的小孩布置暑假或寒假作业。

You can generate a problem set for elementary arithmetic, might useful for parents of primary school student if you don't want to see them too free during summer or winter vocation.

**这个工具有两种用法**

**Usage**

1，运行``python3 run.py``，会打开一个基于``tkinter``制作的UI界面，直接在里面设置参数，然后点击``保存设置``，状态窗口显示“已保存设置！”后点击``生成题集``，状态窗口显示“已生成题目集！”后，即可在设定好的目录下找到问题集和答案。

1, run ``python3 run.py``, and a UI windows would be open, set your parameters there, and click the first button on the left below, after the status window shows a Chinese sentence, that means the parameters are saved, and then click the second button, then the status window would show another Chinese sentence, after that, you can find your problem set and corresponding answer in presetted directory. By the way, the third button would reset your settings if you have not save your settings.

2，如果你具有基础的英文水平，可以打开``conf.json``，根据需要直接修改参数，然后运行``python3 problemset.py``。

2, if you can understand fundamental English, (if you are reading this line, of course you do), just open ``conf.json`` to modify parameters, then run ``python3 problemset.py``.

请保留``conf_tpl.json``，从而保证在某些错误修改设置参数导致程序出错后，能够快速地通过复制粘贴修复好此工具。

Please keep ``conf_tpl.json`` unchanged to ensure you can quickly fix this tool after some unexpected changes of configures.

**未来将会新增的功能**

**Features in the future**

1，英文版本；

1, English version;

2，小数除法；

2, division with decimal;

3，保存与打开自定义设置。

3, save and load custom settings.

**本工具只是我的一个编程练习，我只能保证用户不瞎搞的情况下对用户的计算机不会造成损害，不保证用户瞎搞的情况下会发生什么意想不到的事，也不保证程序设计的逻辑的完全正确。如果这个程序能够帮到你，那可再好不过了。^^**

**I write this tool for programing learning, and I can only guarantee that the user will not cause damage to the his or her computer if he or she dose not suck, but if he or she does so, I could only hope that bad things would not happen. I don't guarantee that the logic of the program design is completely correct. If this tool can help you, that would be great.^^**
