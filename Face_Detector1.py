import cv2
from random import randrange

#Załadowanie przetrenowanych danych z cv2 pliku "haar..."

#Classifier - face detector classifies it as face
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#To capture video from camera / albo film ''HEHE BOI.mp4' zamiast 0
webcam = cv2.VideoCapture(0)

#While loop iteracja po klatkach forever
while True:

    ### Read the current frame - frame to image
    successful_frame_read, frame = webcam.read()
    #Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Detect Faces
    faces_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, w, h) in faces_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 10)

    cv2.imshow('Clever Programmer', frame)

    key = cv2.waitKey(1) #Każda ramka będzie się dziać co 1ms i klika przycisk co 1ms automatycznie aby przeszedl do następnej klatki

    #Stop lower or upper case Q key
    if key==81 or key==113:
        break

#### Release camera object - clean

webcam.release()

#Tylko black and white algorytm zadziała - kolorowe dla lepszego algorytmu wielu osób
#FUNKCJA CVTCOLOR CONVERTCOLOR
"""grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces bez względu jak duże są twarze detectmultiscale - pokaż koordynaty a później narysujemy ten kwadrat dookoła
faces_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


#Drukowanie kwadratów - dla zdjęć z wieloma twarzami mamy pętle
#for (x, y, w, h) in faces_coordinates: # pętla dla wielu
    #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# koordynaty kwadratu ręcznie, 0, 255 kolor zielony - to jest bgr oraz grubość kwadratu 2
#Dodaje 386 aby utworzyć kwadrat na bazie koordynatów twarzy
#cv2.rectangle(img, (428, 84), (428+386, 84+386), (0, 255, 0), 2) przyjład działjący na zmiennych wpisywanych ręcznie do tworzonego kwadratu
#(x, y, w, h) = faces_coordinates[0]
#Automatycznie przypisze zmienne do 4 koordynatów
#cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#(x, y, w, h) = faces_coordinates[1]
#Automatycznie przypisze zmienne do 4 koordynatów
#cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#(x, y, w, h) = faces_coordinates[2]
#Automatycznie przypisze zmienne do 4 koordynatów
#cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


for (x, y, w, h) in faces_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 10)


#print(faces_coordinates)

#Do pokazania zdjęcia imageshow imshow
cv2.imshow('Clever Programmer', img)
cv2.waitKey() #Czekaj z zdjęciem inaczej bez tego się zamknie okno odrazu

"""



print("Code Completed")