# AI-Invigilator

Project aim is to create a series of models which takes in processed videos and examine the frames in order to detect and identify potential cheating behavior. The result whould show candidiate images with suspicious activity.

Project is based on Transfer Learning method wherein pretrained VGG16 model is used as a base model for training purpose. 3 different objects Mobile, Printed Text and Helping Person have been used to classify cheating instance. Django web-framework is used to deploy the project.


Model Outline :-

    1. Entire model is divided into three different modules. 
    
        1. First module is to capture videos of candidates at regular intervals during exam time. Python class "live_caputring" is created which has 2 fucntions namely
       "live_video_capturing" and "convert_vid_to_images". Option to maintain 'Exam Start Time, 'Exam End Time', 'sleep time' and 'video capturing duration' is also provided.
       
        2. Second modules is to classify the cheating instances. Based on pre-trained VGG16, final model is trained and saved as "final_model1.h5"
    
        3. Third module is to display cheating instance. Customized function "pred_inst" is created in django for this purpose.

    2.  Function "pred_inst" first calls "AI_Invigilator_Record.py" having class "live_capturing" which retruns video and images of candidates captured during exam duration.

    3.  Function "pred_inst" then calls "final_model1.h5" which detects cheating instances and display in the web page named "result_page.html". Web page currently shows only 10
        images at one time which is restricted using javascript.
    
    

Work In Progress :-

    1. Currently working on different models creation to compare models and improve accuracy.


Future Path :-

    1. Emailing module needs to be created where cheating instances of candidates can be directly reported to exam supervisor for verification and further action.

    2. Website from login page till exam paper to be created where multiple user can attempt exam at same time.


Technologies and Methods Used :-

    1.  Python - OpenCV, Keras
    2.  Django Webframework
    3.  Javascript


Attachments :-

     1.  Zip file 'vircapstone.zip' contains entire folder having all the necessary files except "final_model1.h5" as the file size was beyond 25 MB. 'AI_Invigilator_Train.py"            file can be used to generated "final_model1.h5".

     2.  Other python files have been attached for reference purpose.
