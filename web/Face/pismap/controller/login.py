from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import os,base64
import datetime
from fr import AFRTest
# AFRTest这个，其中两个dll文件，在Web目录和非Web目录中路径不同，这个要注意

def page(request):
    return render(request, "login.html")

def getface(request):
    if request.POST:
        time = datetime.datetime.now().strftime('%Y%m%d&%H%M%S')
        strs=request.POST['message']
        print(strs)
        imgdata = base64.b64decode(strs)
        
        try:
            file = open(u'static/facedata/confirm/'+time+'.jpg', 'wb')
            file.write(imgdata)
            file.close()
        except:
            print('as')
        res=AFRTest.checkFace(u'static/facedata/base/niewzh.jpg',u'static/facedata/confirm/'+time+'.jpg')
        if res>=0.6:
            return HttpResponse('panel')
        else:
            return HttpResponse('no')
    else:
        return HttpResponse('no')
