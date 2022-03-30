from django.http import response, HttpResponse, JsonResponse
from django.shortcuts import render

import base64
import json

# 需要安装PIL，它是一个图像处理库。安装语句：pip install pillow  安装方法参考上面安装django
import os
from io import BytesIO
import numpy as np
from PIL import Image
import cv2 as cv
import uuid

# import classifyer as classifyer
from . import classifyer_ms as classifyer


net = classifyer.ClassifyerClass()
face_detector = classifyer.FaceDetector()

def score_post_form(request):
    context = {}
    if request.POST:
        if 'Photo' in request.FILES:

            img_file = request.FILES['Photo']
            img_name = os.path.join("static/images", str(img_file))

            # img1 = imageio.imread(img_file)
            # img1 = Image.fromarray(np.array(img1))  # np.uint8(img1)
            # img1.save(img_name)

            img2 = Image.open(img_file).convert('RGB')
            img2_ndarray = np.array(img2)
            faces = face_detector.face_detection(img2_ndarray)
            for x, y, w, h in faces:
                # 在原图像上绘制矩形标识
                cv.rectangle(img=img2_ndarray, pt1=(x, y), pt2=(x+w, y+h), color=(255, 0, 0), thickness=2)

            img2_face = Image.fromarray(img2_ndarray)
            img2_face.save(img_name) 
                    
            if faces != ():
                
                beauty_score = net.recognize(img2) # for pytorch input PIL.Image
                context['Photo'] = img_name
                # context['target_img'] = img_name

                context['beauty'] = beauty_score
            else:
                context['Photo'] = img_name 
                context['beauty'] = "未检测到人脸"

    # context['age'] = 18

    print(context)

    return render(request, "face_score.html", context)


def score_post(request):
    context = {}
    context['msg'] = 'ok'
    context['beauty'] = str(5.0)

    if request.POST:
        # time = datetime.datetime.now().strftime('%Y%m%d&%H%M%S')
        img_name = os.path.join("static/images", str(uuid.uuid1())+".jpg")
        strs=request.POST['image']
        # print(strs)

        #将base64格式的jpg解码成bytes
        img_data = base64.b64decode(strs)    
        #将bytes结果转化为字节流
        bytes_stream = BytesIO(img_data)
        # with open(img_name, 'wb') as file:
        #     file.write(img_data)
        # img = Image.open(img_name).convert('RGB')
        img = Image.open(bytes_stream).convert('RGB')
        img_ndarray = np.array(img)
        faces = face_detector.face_detection(img_ndarray)
        
        # img.save(img_name)

        if faces != ():

            beauty_score = net.recognize(img) 
            context['beauty'] = str(beauty_score)
            context['faces'] = faces[0].tolist()
            
        else:
            context['msg'] = 'face not found'

    # context['age'] = 18

    print(context)

    return JsonResponse(context)

def video(request):
    return render(request, "video.html")

def index(request):
    return render(request, "face_score.html")