# OpenCV

## Facial & Human Body detection

This OpenCV application is using basic methods to detect human faces and bodys via webcam.

### Requirements
* OpenCV 3.1 (https://opencv.org/releases.html)
* Python 2.7.XX (https://www.python.org/downloads/)
* Numpy 1.8.0 (http://sourceforge.net/projects/numpy/files/NumPy/)

# Tutorial 
In the following tutorial I will show you how to set up the environment to work/run on this project. This is one of the multiple ways to set the project up, if you find another better way for yourself -> skip this! 

### 1. You will need.
* OpenCV, Python and Numpy in the defined versions. 
* Java Runtime Environment (JRE8) http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html
* Eclipse Java EE IDE https://www.eclipse.org/downloads/
* PyDev in Eclipse. Open Eclipse->Help->Install new software->Work with->http://pydev.org/updates

### 2. Using correct paths.
I was using a Windows mashine, when you are using Linux or Mac the paths will be different. 
 
In case: 
Python installation path: C:\Python27.XX
After extracting the OpenCV archive you will find a file named "cv2.pyd". Copy this file into the following paths.
* C:\opencv3.1\build\python\2.7\x86
* C:\Python27\Lib\site-packages

Copy the file "haarcascade_frontalface_default.xml" into 
* C:\opencv3.1\build\etc\haarcascades 

### 3. Start the Python IDLE/ Bash.
If you can import OpenCV and Numpy without any error message your integration was successful. If not go back two steps. 
```
import cv2
import numpy
```
### 4. Start Eclipse.
Navigate to Eclipse-> Window-> Preferences-> PyDev-> Interpreters -> Python Interpreter -> Choose: "C:\Python27\python.exe" 

### 5. Import the Project files & RUN.


