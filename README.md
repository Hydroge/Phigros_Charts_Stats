# Phigros_Charts_Stats

To summarize the information of every charts in Phigros.

## `Transform.py` 使用方法

首先将自己的谱面重新命名，序列化为从1到n（n为一个文件夹内，不包含子目录的谱面的数量）。

然后启动该软件，直接输入路径和谱面的数量，程序就会寻找谱面物量数和第一时间的BPM值，将其写在文件名称上。方便日后参照萌娘百科等文献以比对。

若想添加难度，建议直接在文件名称前面添加`EZ-``HD-``IN-``AT-``LE-``SP-`。或者在`.json`前面添加`-EZ`等。

## `Chart_Stats.py·` 使用方法

首先确保自己的谱面文件是存放在一个文件夹内的。并且格式为`EZ-XXX-YYY.json`。

其中`EZ`可以替换成`HD``IN`等上文提到过的难度，`XXX`为物量，`YYY`为BPM，且不一定为3位数（这里程序会自动处理好）。

然后就会生成一张关于谱面简要信息的`.csv`文件。

## `result.csv` 使用方法

这是本人已经统计好的物量信息和BPM，仅供参考。由于部分谱面的物量数和BPM相同，暂时无法直接自动处理文件。