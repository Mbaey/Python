from fr import AFRTest
from django.http import HttpResponse

def face(request):
    res = AFRTest.checkFace(u'static/facedata/base/niewzh.jpg', u'static/facedata/base/niewzh.jpg')
    return HttpResponse(res)