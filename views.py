from django.shortcuts import render
from django.http import HttpResponse
from .apps import DlappConfig
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.conf import settings
from subprocess import run, PIPE

import cv2
import os
import requests
import sys
import numpy as np


def pred_inst(request):

    out_img = run([sys.executable,'AI_Invigilator_Record.py'],shell=False,stdout=PIPE)

    fls = os.listdir(settings.OUT_PATH)
    fss = FileSystemStorage()
    all_images_url = []

    if len(fls) > 0:

        for i in fls:

            # load the image
            img = os.path.join(settings.OUT_PATH, i)
            img12 = cv2.imread(img, cv2.IMREAD_COLOR)

            # resizing the image
            img12 = cv2.resize(img12, (224, 224))
            img11 = np.array(img12)
            img11 = np.expand_dims(img11, axis=0)

            test_result = np.round(DlappConfig.predictor.predict(img11))
            print('Test result is : ',test_result)

            if test_result[0][0] == 1:

                print("Non Cheating Instance")

            else:

                #image_name = fss.save(i,File(open(img,'rb')))
                image_url = fss.url(img)
                print('image url is',image_url)
                all_images_url.append(image_url)
                print("Cheating Instance")

        print("existing ml_predict function")

        return render(request,'result_page.html', {'data': all_images_url,'img_url': settings.MEDIA_URL})

# Create your views here.
