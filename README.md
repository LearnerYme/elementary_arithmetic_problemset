# elementary_arithmetic_problemset
你可以使用这个小学生算术题生成器来自动产生很多道给小学生做的加减乘除题目。比如给你的小孩布置暑假或寒假作业。

You can generate a problem set for elementary arithmetic, might useful for parents of primary school student if you don't want to see them too free during summer or winter vacation.

***

Version 1.1.1

修复了一个bug。

Fixed a bug.

***

Version 1.1.0

增加了英文版。

English version is now available.

修复了一些bug。

Fixed some bugs.

更新了README。

Updated README.

**这个工具有三种用法**

**Usage**

1，运行``sh run.sh``并选择语言参数：zh，ZH，CN和Chinese。随后会出现一个基于``tkinter``制作的UI界面，直接在里面设置参数，然后点击``保存设置``，状态窗口显示“已保存设置！”后点击``生成题集``，状态窗口显示“已生成题目集！”后，即可在设定好的目录下找到问题集和答案。点击``重置设置``可以恢复保存前的设置。

1, run ``sh run.sh`` and choose a language argument: en, EN or English. And a UI window would be open, set your parameters for problem set, and click ``SAVE`` to save your settings, after the status window shows 'Settings saved!', click ``SUBMIT`` to generate problem set. If you don't want to save your settings, click ``RESET`` to recover.

2，直接运行``python3 run_zh.py``，进入UI界面设置、保存并生成。

2, run ``python3 run_en.py`` to open that UI window and do the rest steps.

3，如果你能看懂``conf.json``中的设置项，可以直接设置，保存后运行``python3 problemset.py``。

3, if you can understand parameters in ``conf.json``, you can directly modify them and run ``python3 problemset.py`` after saving.

请保留``conf_tpl.json``，从而保证在某些错误修改设置参数导致程序出错后，能够快速地通过复制粘贴修复好此工具。

Please keep ``conf_tpl.json`` unchanged to ensure you can quickly fix this tool after some unexpected changes of configures.

除此以外，暂时不支持保存多个自定义设置，但你可以修改``conf.json``并另存为其他名字比如``confname.json``，然后运行``python3 problemset.py -conf confname.json``。

What's more, you cannot save multiple custom settings yet, but you can modify ``conf.json`` and save as another file, for example, ``confname.json``, then run ``python3 problemset.py -conf confname``.

***

Version 1.0

**这个工具有两种用法**

**Usage**

1，运行``python3 run.py``，会打开一个基于``tkinter``制作的UI界面，直接在里面设置参数，然后点击``保存设置``，状态窗口显示“已保存设置！”后点击``生成题集``，状态窗口显示“已生成题目集！”后，即可在设定好的目录下找到问题集和答案。

1, run ``python3 run.py``, and a UI window would be open, set your parameters there, and click the first button on the left below, after the status window shows a Chinese sentence, that means the parameters are saved, and then click the second button, then the status window would show another Chinese sentence, after that, you can find your problem set and corresponding answer in presetted directory. By the way, the third button would reset your settings if you have not save your settings.

2，如果你具有基础的英文水平，可以打开``conf.json``，根据需要直接修改参数，然后运行``python3 problemset.py``。

2, if you can understand fundamental English, (if you are reading this line, of course you do), just open ``conf.json`` to modify parameters, then run ``python3 problemset.py``.

请保留``conf_tpl.json``，从而保证在某些错误修改设置参数导致程序出错后，能够快速地通过复制粘贴修复好此工具。

Please keep ``conf_tpl.json`` unchanged to ensure you can quickly fix this tool after some unexpected changes of configures.

***

**未来将会新增的功能**

**Features in the future**

1，英文版本；已完成！

1, English version; Done!

2，小数除法；

2, division with decimal;

3，保存与打开自定义设置。

3, save and load custom settings.

**本工具只是我的一个编程练习，我只能保证用户不瞎搞的情况下对用户的计算机不会造成损害，不保证用户瞎搞的情况下会发生什么意想不到的事，也不保证程序设计的逻辑的完全正确。如果这个程序能够帮到你，那可再好不过了。^^**

**I write this tool for programing learning, and I can only guarantee that the user will not cause damage to the his or her computer if he or she dose not suck, but if he or she does so, I could only hope that bad things would not happen. I don't guarantee that the logic of the program design is completely correct. If this tool can help you, that would be great.^^**
