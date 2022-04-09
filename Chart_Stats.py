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

headers = ['Name', 'Difficulty', 'Notes', 'BPM']    # 谱面的基本信息：名字、难度、物量、节拍
diffs = ['EZ', 'HD', 'IN', 'AT', 'LE', 'SP']        # 六大难度

totalStats = []                                     # 待写入到文件的总数据

def execute_files():
    currentPath = os.getcwd()                       # 获得脚本所在目录
    for _, dirs, _ in os.walk(currentPath):         # 遍历当前目录
        for dir in dirs:                                                # 遍历每一个子目录，其实就是访问一个个歌曲文件夹
            currentSubPath = os.path.join(currentPath, dir)             # 设定子目录
            isChart = False                                             # 有的文件夹并不是谱面文件夹
            for _, _, files in os.walk(currentSubPath):                 # 提取该歌曲文件夹内的全部文件
                for file in files:                              # 对每一个子目录当中的文件进行遍历
                    chartData = {}                              # 待写入总数据的一条条信息
                    chartData['Name'] = dir                     # 谱面名称
                    for diff in diffs:                          # 对难度进行遍历
                        if 'fake' in file:                      # 望影方舟谱面当中，多了几个音符的谱面让我打上了fake标记，不是该统计的部分。
                            continue
                        if diff in file:                        # 如果在名称中找到难度字符的字符，就采集信息。
                            isChart = True
                            chartData['Difficulty'] = diff
                            dataString = file[3:-5]
                            dataString = dataString.split('-')
                            chartData['Notes'] = dataString[0]
                            chartData['BPM'] = dataString[1]
                    if isChart:                                 # 是谱面文件的话就收集，不是谱面文件的话就不操作
                        print(chartData)
                        totalStats.append(chartData)
    print(totalStats)

    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(totalStats)

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
                    if isChart:
                        print(chartData)
                        totalStats.append(chartData)
    print(totalStats)

    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(totalStats)

if __name__ == "__main__":
    method=input('''Please select the method. "f" means collect 
    ''')
    initTime=time.time()
    execute_diffs()
    print("Running time: {0}".format(time.time()-initTime))