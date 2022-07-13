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
from ctypes import sizeof
import os
import time
import json
import jsonpath
import zipfile

headers = ['Name', 'Difficulty', 'Notes', 'BPM', 'Tap', 'Drag', 'Hold', 'Flick']    # 谱面的基本信息：名字、难度、物量、节拍
diffs = ['EZ', 'HD', 'IN', 'AT', 'LE', 'SP']        # 六大难度

totalStats = []                                     # 待写入到文件的总数据

def execute_folders(target):
    #currentPath = os.getcwd()                                       # 获得脚本所在目录
    currentPath = target
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
                        if diff in file and ".json" in file:
                            isChart = True
                            dataString = file[3:-5]
                            dataString = dataString.split('-')
                            chartData.append(dataString[0])
                            chartData.append(dataString[1])

                            #这里本来要对Demiurge的BPM作特殊调整，但考虑到本人整合信息的时候不使用文件夹形式，因此不在这里赘述代码了。#

                            '''
                            以上操作是通过读取文件名的方式获取谱面的物量和初始BPM信息，接下来的部分是获取每个谱面的详细物量
                            也就是Tap, Drag, Hold, Flick这四种音符各自有多少个
                            '''

                            with open(os.path.join(currentSubPath, file), mode="r") as f:
                                #print("Opening: {0}".format(os.path.join(currentSubPath, file)))
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
                                    print("错误：四种音符数量的总和不等于谱面总物量！")
                                f.close()
                    if isChart:
                        print(chartData)
                        totalStats.append(chartData)
                        
    #print(totalStats)

    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(totalStats)

def execute_zips(target):
   #currentPath = os.getcwd()
    currentPath = target
    for _, _, files in os.walk(currentPath):
        for file in files:  #打开当前文件夹的zip文件
            filePath = currentPath + os.sep + file
            if zipfile.is_zipfile(filePath):    #检验是不是zip文件
                with zipfile.ZipFile(filePath, 'r') as z:   #打开zip文件
                    nameList = z.namelist()     #压缩文件内的文件名目录
                    for diff in diffs:          #按照难度进行排序
                        beatmap_gotten = False  #是否得到当前难度的谱面？
                        for fileInside in nameList: #对每个压缩包内文件进行遍历
                            fileInsideName = fileInside.replace(nameList[0], '')    #将前面的路径删掉
                            if '.json' not in fileInsideName:   #.json不在文件名内，说明不是官方谱面文件
                                continue
                            if diff not in fileInsideName:  #难度不在文件名内，说明不是谱面文件
                                continue
                            if 'fake' in fileInsideName:    #fake特殊标记在文件名内，自动忽略
                                continue
                            beatmap_gotten = True
                            chartData = []
                            chartData.append(file.replace(".zip", ''))  #曲名取自zip文件的压缩包名

                            __songname = file.replace(".zip", '') #取曲名，可能会有特殊条件

                            chartData.append(diff)
                            dataString = fileInsideName[3:-5]
                            dataString = dataString.split('-')
                            chartData.append(dataString[0])

                            if __songname == "Demiurge":        # Demiurge 的BPM随谱面难度不同而不同，需要格外注意。
                                dataString[1] = "111"

                            chartData.append(dataString[1])

                            with z.open(fileInside, mode="r") as f:
                                #print("Opening: {0}".format(fileInside))
                                fileRead = f.read().decode('utf-8')
                                jsonLoad = json.loads(fileRead)

                                #print(jsonLoad)
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
                                    print("错误：四种音符数量的总和不等于谱面总物量！")
                                f.close()

                        if beatmap_gotten:
                            print(chartData)
                            totalStats.append(chartData)
                    z.close()

    #print(totalStats)
    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(totalStats)
        f.close()

if __name__ == "__main__":
    #debug__=os.getcwd()
    _method = '0'
    targetPath = input("Beatmap Path 谱面目录:")

    while _method not in ['f', 'F', 'z', 'Z']:
        _method = input('''
Please type the method of extracting beatmap files.
"Z" means to load every .zip files, and "F" means to load every folders.
This program is not case-sensitive.
请输入提取谱面文件的方式字：Z代表提取压缩文件，F代表提取文件夹。该操作大小写不敏感。
''')

    initTime=time.time()
    if _method in ['f', 'F']:
        execute_folders(targetPath)
    elif _method in ['Z', 'z']:
        execute_zips(targetPath)
    print("Found {0} beatmaps.".format(len(totalStats)))
    print("Running time: {0}".format(time.time()-initTime))
    