# -*- coding: utf-8 -*-
import json
import os
import urllib.request
import threading
import sys
def Schedule(a,b,c):#下载进度指示
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)
    
def download_thread(url, name):
    try:
        print("Downloading "+name)
        urllib.request.urlretrieve(url, name, Schedule)
    except Exception as e:
        log = open("log.txt", "w+")
        log.write(url,"\t" ,name)
        log.flush()
        log.close()
        print ("Error: ",e)

def getMOOCLessons(jsonObj):
    courseName=jsonObj['results']['courseDto']['name']+" "+jsonObj['results']['courseDto']['schoolName']
#    os.mkdir(courseName)  # 创建名称为“课程名+校名”的根目录

    if(os.path.exists(courseName)==False):
        os.mkdir(courseName)

    chapters=jsonObj['results']['termDto']['chapters']#读取所有章节的信息为一个列表
    for i in range(len(chapters)):#遍历所有章节
        if(os.path.exists(courseName + '\\' + chapters[i]['name']) == False):
            os.mkdir(courseName + '\\' + chapters[i]['name'])#每一个章节建立一个文件夹

        print(chapters[i]['name'])

        lessons=chapters[i]['lessons']#读取当前章节下所有课时的信息为一个列表
        for j in range(len(lessons)):#遍历所有课时
            units=lessons[j]['units']#读取当前课时下所有小节的信息为一个列表
            for k in range(len(units)):#遍历所有小节
                aunit=units[k]
                if (aunit["contentType"]==1):#判断该小节是否为视频内容
                    download_thread(aunit["resourceInfo"]["videoHDUrl"], courseName + '\\' + chapters[i]['name']+'\\'+str(k)+'.'+aunit['name']+".mp4")
                    
#os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
#urllib.request.urlretrieve(, Schedule)#下载文件，这里下载的是高清资源

if __name__  == "__main__":
    if (len(sys.argv) > 1):
        print("Start Download Mooc：" + sys.argv[1])
        jsonFile = open(sys.argv[1] , encoding='UTF-8').read()  # 事先将抓包所得的json保存为同目录下的文本文件
        jsonObj = json.loads(jsonFile)
        getMOOCLessons(jsonObj)
    if(1==2):
        complex;