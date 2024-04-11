import cv2
import mediapipe as mp #face detect when video running
import pyautogui # move mouce 

cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)# refine rand marks five 478 land marks so identyfy the eyes
screen_w,screen_h=pyautogui.size()
while True:
    _,frame=cam.read()
    frame=cv2.flip(frame,1)# frame eka harawanawa verically
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)# convertion issier wehen color is same that why convert same color
    output=face_mesh.process(rgb_frame)   # create a out from rgb frame
    landmark_points=output.multi_face_landmarks # detecting lots of thing in face like nose mouse like wise
    # print(landmark_point)

    frame_w,frame_h,_=frame.shape

    if landmark_points:
        landmarks=landmark_points[0].landmark # detecting only one face
         # we need to identify where is the land marks
        for id,landmark in enumerate(landmarks[474:478]):#it will give eye, enumerate give you a two thing id and landmark
            # x= landmark.x # getting every land marks coordinates. this shows position on the screen. its shows fraction numbers
            # y=landmark.y# so frame have to be bigger so have to multyfy with height and with
            x=int(landmark.x*frame_w)# its getting intreger numbers 
            y=int(landmark.y*frame_h)
            # we have to detect the center its easy have to drwa a circle
            cv2.circle(frame,(x,y),3,(0,255,0))# where is the draw circle, second wher is the center, third one is radius , fourth one is color RGB
        # now you can see lots of land mark in your face
        #id eka change weddi cursor eka move wenna one
            if id==1: 
                screen_x = screen_w * (x / frame_w)
                screen_y = screen_h * (y / frame_h)
                pyautogui.moveTo(screen_x, screen_y)
        # print(x,y)

        left=[landmarks[145],landmarks[159]]
        for landmark in left:
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)

            cv2.circle(frame,(x,y),3,(0,255,255))
        
        if(left[0].y-left[1].y)<0.004:# weenedd to point only y for detect click from verticel access 
            # print('click')
            pyautogui.click()
            pyautogui.sleep(1)
    

    cv2.imshow('eye control mouse',frame)
    # cv2.waitKey(1)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break