# coding=UTF-8

'''
谱面文件的格式为：一个文件夹，里面包含若干个.json格式的谱面文件。
譬如一个谱面文件是这样的格式：

Mobilys\
    EZ-311-144.0.json
    HD-530-144.0.json
    IN-938-144.0.json
    Mobilys.png
    Mobilys.wav

那么所有.json的文件就是谱面文件。而该程序所做的就是将谱面文件的信息提取并生成一个.csv文件。
execute_files()以AT EZ HD IN LE SP为顺序进行整理。
execute_diffs()以EZ HD IN AT LE SP为顺序进行整理。
'''

import csv
import os
import time
import json
import jsonpath

headers = ['Name', 'Difficulty', 'Notes', 'BPM', 'Tap', 'Drag', 'Hold', 'Flick']    # 谱面的基本信息：名字、难度、物量、节拍
diffs = ['EZ', 'HD', 'IN', 'AT', 'LE', 'SP']        # 六大难度

totalStats = []                                     # 待写入到文件的总数据

def execute_diffs():
    currentPath = os.getcwd()                                       # 获得脚本所在目录
    for _, dirs, _ in os.walk(currentPath):                         # 遍历当前目录
        for dir in dirs:                                            # 遍历每一个子目录，其实就是访问一个个歌曲文件夹
            currentSubPath = os.path.join(currentPath, dir)                     # 设定子目录
            for _, _, files in os.walk(currentSubPath):             # 提取该歌曲文件夹内的全部文件
                for diff in diffs:
                    chartData = []
                    isChart = False
                    chartData.append(dir)
                    chartData.append(diff)
                    for file in files:
                        if 'fake' in file:
                            continue
                        if diff in file:
                            isChart = True
                            dataString = file[3:-5]
                            dataString = dataString.split('-')
                            chartData.append(dataString[0])
                            chartData.append(dataString[1])

                            '''
                            以上操作是通过读取文件名的方式获取谱面的物量和初始BPM信息，接下来的部分是获取每个谱面的详细物量
                            也就是Tap, Drag, Hold, Flick这四种音符各自有多少个
                            '''

                            with open(os.path.join(currentSubPath, file), mode="r") as f:
                                print("Opening: {0}".format(os.path.join(currentSubPath, file)))
                                fileRead = f.read()
                                jsonLoad = json.loads(fileRead)

                                # 获取谱面物量信息，会形成一个含有 1 2 3 4 这四个数字的列表。这四个数字分别代表上述的四种音符。
                                types_above = jsonpath.jsonpath(jsonLoad, "$.judgeLineList[*].notesAbove[*].type")
                                types_below = jsonpath.jsonpath(jsonLoad, "$.judgeLineList[*].notesBelow[*].type")
                                # print(types_above, types_below)
                                # 有的谱面没有从判定线地下浮上来的音符，因此结果是False．这个时候再直接与数组相加的话会报错
                                types = []
                                if types_above != False:
                                    types += types_above
                                if types_below != False:
                                    types += types_below
                                # 该谱面音符信息综述。统计每个音符在列表当中的次数
                                noteResult = []
                                for i in range(1, 5):
                                    noteResult.append(str(types.count(i)))
                                # 如果统计过程中的音符数与从文件当中获取的音符数不相符，就不会再录入
                                try:
                                    if len(types) != int(dataString[0]):
                                        raise Exception('NoteAmountNotEqual')
                                    chartData = chartData + noteResult
                                except Exception:
                                    print("ERROR: Note amount not Equal (notes != tap+drag+hold+flik)")
                                f.close
                    if isChart:
                        print(chartData)
                        totalStats.append(chartData)
    print(totalStats)

    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(totalStats)

if __name__ == "__main__":
    initTime=time.time()
    execute_diffs()
    print("Running time: {0}".format(time.time()-initTime))