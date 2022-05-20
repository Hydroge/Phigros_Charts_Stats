# Phigros_Charts_Stats （中文）

![](https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-nc-nd.png)

**注意：本数据集遵循[署名-非商业性使用-禁止演绎 3.0 未本地化版本 (CC BY-NC-ND 3.0)](https://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh)协议。若转载、复制、发行本作品等，请附上原文出处链接及本声明。**

本仓库总结了Phigros当中每个谱面的一些信息，包括BPM和物量。同时在这里也提供了一些方便扒谱的工具。

想查看任何已经存在的谱面之变动，可以移步到`changes.md`文件中。

如果有任何问题欢迎在答疑区（Issues）提出。

祝扒谱快乐！

## `Transform.py` 使用方法

首先将自己的谱面(.json)重新命名，序列化为从1到n（n为一个文件夹内，不包含子目录的谱面的数量）。

然后启动该软件，直接输入路径和谱面的数量，程序就会寻找谱面物量数和第一时间的BPM值，将其写在文件名称上。方便日后参照[萌娘百科](https://zh.moegirl.org.cn/Phigros/%E8%B0%B1%E9%9D%A2%E4%BF%A1%E6%81%AF)或本仓库的`result.csv`等文献以比对。

若想添加难度，建议直接在文件名称前面添加`EZ-` `HD-` `IN-` `AT-` `LE-` `SP-`。或者在`.json`前面添加`-EZ`等。

## `Chart_Stats.py` 使用方法 

**现在该代码支持自定义谱面文件目录。**

谱面文件的格式为：一个文件夹，里面包含若干个.json格式的谱面文件。（如果要处理自制谱的话还请阁下自己修改代码了）

譬如一个谱面文件是这样的格式：

```
Mobilys\
    EZ-311-144.0.json
    HD-530-144.0.json
    IN-938-144.0.json
    Mobilys.png
    Mobilys.wav
```

首先确保自己的谱面文件是存放在一个文件夹内的。并且格式为`EZ-XXX-YYY.json`。其中`EZ`可以替换成`HD` `IN`等上文提到过的难度，`XXX`为物量，`YYY`为BPM，且不一定为3位数（这里程序会自动处理好）。

那么所有.json的文件就是谱面文件。而该程序所做的就是将全部谱面文件的信息提取并生成一个.csv文件。

该程序现在支持.zip文件，且可以统计四种音符的数量。

## `result.csv` 使用方法 

这是本人已经统计好的物量信息和BPM，仅供参考。由于部分谱面的物量数和BPM相同，暂时无法直接自动处理文件。

值得一提的是，由于有些歌对大多数用户难以输入，本表对其进行了改动。包括但不限于：

- 某些简繁混搭的曲目将全部使用简体中文来表示（《華灯爱》——《华灯爱》）。
- 过于复杂的歌名将只取前面几个单词（《Infinite Enerzy -Overdoze-》——《Infinite Enerzy》）。
- 如果歌名是日文：
  - 带汉字的，将只取汉字部分（《雪降り、メリクリ》——《雪降》）。
  - 纯日文平假名的，使用罗马字（《もぺもぺ》——《Mopemope》）。
  - 纯日文片假名的，使用其英文形式（《ジングルベル　Jingle Bell》——《Jingle Bell》）。
- 如果歌名为希腊文的：
  - 采取转写（《Ποσειδών》——《Poseidon》）。
- 歌名是一片符号的：
  - 有可识别英文单词的，取英文单词（《Cipher》）。
  - 本身就是魔改的，取英文原意（《ρars/ey》——《parsley》）。

- - -

# Phigros_Charts_Stats （English）

![](https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-nc-nd.png)

**CAUTION: THIS DATASET IS APPLIED BY [Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)](https://creativecommons.org/licenses/by-nc-nd/3.0/). If you copy, reproduce, distribute this work, etc., please attach a link to the original source and this statement.**

To summarize the information of every beatmaps in Phigros, including BPM and note amount. Also, some tools are provided here, which can help you to extract beatmap files more easily.

If you want to have a look at any changes of existing beatmaps, please check `changes.md`.

If you have any problems, feel free to communicate in "Issues".

Have fun digging!

## Usage of `Transform.py`

First, rename your own beatmap files (.json) and serialize them from 1 to n (n is the number of beatmap files in a folder, excluding subdirectories).

Then start the program, directly input the path and the number of beatmap files, the program will find the note amount and the **initial** BPM of each beatmap file, and rename them to `Notes-BPM.json`. It is convenient to refer to [Details of beatmaps](https://zh.moegirl.org.cn/Phigros/%E8%B0%B1%E9%9D%A2%E4%BF%A1%E6%81%AF) or `result.csv` in this repository for comparison in the future.

If you want to add difficulty, it is recommended to add `EZ-` `HD-` `IN-` `AT-` `LE-` `SP-` directly before the file name. Or add `-EZ` in front of `.json`, etc.

## Usage of `Chart_Stats.py`

**Right now this program has supported customized path of beatmaps.**

The format of the beatmap file is: a folder containing several beatmap files in .json format. (If you want to deal with fanmade beatmaps, please modify the source code yourself)

For example, a beatmap file has the following format:

```
Mobilys\
    EZ-311-144.0.json
    HD-530-144.0.json
    IN-938-144.0.json
    Mobilys.png
    Mobilys.wav
```

Firstly make sure your beatmap files are stored in a folder. And the format of every beatmaps is `EZ-XXX-YYY.json`, where `EZ` can be replaced with `HD` `IN` and other difficulties mentioned above, `XXX` is the quantity, `YYY` is the BPM, and it is not necessarily a 3-digit number (the program will handle it automatically here).

Then all .json files are beatmap files. What the program does is to extract the information from beatmap files and generate a summarized .csv file.
This program also supports .zip files right now. And it could summarize the detialed amounts of Tap, Drag, Hold and Flick.

## Usage of `result.csv`

This is the note amount and BPM that I have already summarized, for reference only. Since there are some beatmaps share the same note amount and BPM information, it is temporarily impossible to process the files automatically.

Because the name of beatmaps can be in English, Chinese, Japanese and Greek, even in symbols. I would like to rename them myself, for people easier to look up the imformation of a specific beatmap.

- Some mashups of simplified and traditional Chinese will be replaced to Simplified Chinese completely. e.g. 華灯爱 -> 华灯爱
- Overcomplicated song titles will only be taken the first few words. e.g. Infinite Enerzy -Overdoze- -> Infinite Enerzy
- If the title is mainly in Japanese:
  - If it includes Kanji, only Kanji will be considered. e.g. 雪降り、メリクリ -> 雪降
  - Pure Japanese Hiragana, using Romaji. e.g. もぺもぺ -> Mopemope
  - Pure Katakana, using its English form. e.g. ジングルベル　Jingle Bell -> Jingle Bell
- If the title is mainly in Greek：
  - JUST TRANSLITERATE IT. e.g. Ποσειδών -> Poseidon
- If the title includes some symbols：
  - If there are some meaningful words, only take them. e.g. Cipher
  - If the title is originated from a specific word, the original word will be taken. e.g. ρars/ey -> parsley
