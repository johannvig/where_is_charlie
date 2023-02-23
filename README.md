# reconnaissance-faciale

(manque la version utilisant le ML)

This Python script uses the Face Recognition library and PIL library to detect and recognize faces in an image. It first loads a set of known images and their respective encodings. It then loads an unknown image and detects all the faces in that image. It then compares each detected face in the unknown image with the known encodings to identify the name of the person. Finally, it draws a rectangle around each detected face and prints the name of the person.

Libraries used

This script requires the following libraries to be installed:

PIL
face_recognition
numpy


How to run the script


Install the required libraries using pip or conda.
Place the known images and the unknown image in the same directory as the script.
Change the file names in the script to match the names of the images you want to use.
Run the script.
