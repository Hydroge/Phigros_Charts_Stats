#基于python3.10
#代码来自于https://www.bilibili.com/read/cv15503487#reply108566197056
#代码原作者「我觉得你长得很省电」

#加载库
import json
import os

number = 0    #可能把for语句记叉了所以只会用while做循环，定义一个计数变量
workpath = input("请输入铺面位置（绝对路径）：")+"//"
allcount = int(input("请输入总铺面数（即总文件数）："))-1

while number <= int(allcount):
    os.chdir(str(workpath))
    number = number + 1

    try:
        with open("{0}.json".format(number),mode="r") as f:  #打开文件
            s = f.read()
            d = json.loads(s)
            i = d.get("numOfNotes")     #调取物量数据
            j = d.get('judgeLineList')[0].get('bpm')#调取BPM信息
            f.close

        src = os.path.join(workpath,str(number)+'.json')     #记录路径和更改后名字
        #dst = os.path.join(workpath,str(i)+'-'+str(j)+'('+str(number)+')'+'.json')
        dst = os.path.join(workpath, str(i) + '-' + str(j) + '.json')

        os.rename(src,dst)  #更名

        #print(str(number)+".json已处理，结果为："+str(i)+'-'+str(j)+'('+str(number)+')'+'.json')     #输出结果
        print(str(number) + ".json已处理，结果为：" + str(i) + '-' + str(j) + '.json')  # 输出结果

    except:

        print("Error:"+str(number)) 