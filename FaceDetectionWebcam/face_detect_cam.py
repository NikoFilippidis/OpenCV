'''
Created on 15.01.2016

@author: Niko Filippidis
'''
import cv2

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

#Initialize the webcam.
video_capture = cv2.VideoCapture(0)

while True:
    #Get the next frame of the cam.
    ret, frame = video_capture.read()
    
    #Convert the frame to an gray picture for better processing.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Facetedection initialisation.
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    ) 
    
    
    #Draw a rectangle around every found face.  
    for (x, y, w, h) in faces:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
       #Name above the face
       cv2.putText(frame,"Face", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,200,200), 2)
       #Prints the amount of faces in the camera field
       cv2.putText(frame,str(len(faces)), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (0,200,200), 2)
  
   
    #Body detection initialisation
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    foundLocationsOfBody, foundWeights = hog.detectMultiScale(
        frame,
        winStride=(8, 8), 
        padding=(32, 32), 
        scale=1.05
    )
    #Draw a rectangle around every found body.  
    for x, y, w, h in foundLocationsOfBody:
    # Draw rectangle around fond object
        if len (foundLocationsOfBody) > 0:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    
    
    
    
    
    #Create a namedWindow to set flags
    cv2.namedWindow("Stylebox", cv2.WND_PROP_FULLSCREEN)   
    #Setting parameters for the creating windows       
    cv2.setWindowProperty("Stylebox", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
   
    #Display the result
    cv2.imshow("Stylebox", frame)
    
    #Programm break condition 
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Release the webcam 
video_capture.release()
#Close the display window
cv2.destroyAllWindows()
