#!/usr/bin/env python
# coding: utf-8

import cv2
import time
import datetime
from datetime import datetime, timedelta
import random
import numpy as np
import os
from django.conf import settings

exam_start_time = datetime(2021, 1, 10, 20, 21, 0)
exam_end_time = datetime(2021, 1, 10, 20, 23, 0)


class live_capturing:

    print("Entering class live_capturing")

    def live_video_capturing():

        print("Entering function live_video_capturing within class live_capturing")

        ran_time = [5, 10, 15, 25, 30, 50, 60]

        while datetime.now() > exam_start_time and datetime.now() < exam_end_time:

            print("Entering exam time")

            ran_gap = random.choice(ran_time)
            time.sleep(ran_gap)
            file_name = settings.IN_PATH + 'stu_id' + str(time.time()) + '.mp4'
            print(file_name)

            v1 = cv2.VideoCapture(0)

            if (v1.isOpened() == False):
                print("Camera is already running")

            shoot = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'mp4v'),
                                    20, (640, 480))

            record_end_time = datetime.now() + timedelta(seconds=60)

            while datetime.now() < record_end_time:

                ret, frame = v1.read()

                if ret == True:

                    shoot.write(frame)

                else:

                    break

            v1.release()
            shoot.release()
            cv2.destroyWindow

            print("Closing Window")

        cv2.destroyAllWindows()

        print('Exam Over')

    def convert_vid_to_images():

        print("Entering function convert_vid_to_images within class live_capturing")

        fls = os.listdir(settings.IN_PATH)

        if len(fls) > 0:

            for x in fls:

                vid1 = cv2.VideoCapture(settings.IN_PATH + x)
                frame_count = int(vid1.get(cv2.CAP_PROP_FRAME_COUNT))
                #filename = str(time.time()) + '.png'

                for i in range(frame_count):

                    _, img7 = vid1.read()
                    cv2.imwrite(settings.OUT_PATH + str(time.time()) + '.png', img7)

        print("Video to images conversion over")

def main():

    live_capturing.live_video_capturing()
    live_capturing.convert_vid_to_images()

if __name__ == "__main__":
    main()
