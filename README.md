# AI-Invigilator

The goal of our project is to create a series of models which take in processed videos and examine the frames in order to detect and identify potential cheating behavior. The result should show which frames showed suspicious activity so that the corresponding time stamp can be found.

Project is based on Transfer Learning method wherein pretrained VGG16 model is used as a base model for training purpose. 3 different objects Mobile, Printed Text and Helping Person have been used to classify cheating instance. Django web-framework is used to deploy the project.

Model Outline

1. Entire model is divided into three different modules. 
    
    1. One module is to capture videos of candidates at regular intervals during exam time. Python class "live_caputring" is created which has 2 fucntions namely
       "live_video_capturing" and "convert_vid_to_images". Option to maintain Exam Start and End Time, sleep time and video capturing duration is also provided.
       
    2. Second modules is to determine the cheating. Based on pre-trained VGG16, final model is created and saved as "final_model1.h5"
    
    3. Third module is to display cheating instance. Customer function "pred_inst" is created in django for this purpose

2.  Function "pred_inst" first calls "AI_Invigilator_Record.py" having class "live_capturing" which retruns video and images of candidates captured during exam duration.

3.  Function "pred_inst" then calls "final_model1.h5" which detects cheating instances and display in the web page named "result_page.html". Web page currently shows only 10
    images at one time which is restricted using javascript.
    
    
 Work In Progress
 
 

