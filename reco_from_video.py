import cv2
import os
from to_excel import Excel_handle
excel = Excel_handle()
excel.read_excel("Attendance.xlsx")





faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Call the trained model yml file to recognize faces
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trained.yml")

# Names corresponding to each id


names = os.listdir("images")

video_capture = cv2.VideoCapture(0)
while True:
    ret,img = video_capture.read()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray_image, 1.3,5)
    

    # Try to predict the face and get the id
    # Then check if id == 1 or id == 2
    # Accordingly add the names

    for (x, y, w, h) in faces:
        # cv2.rectangle(gray_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, _ = recognizer.predict(gray_image[y : y + h, x : x + w])
        print("id reported",id,"name found",names[id])
        excel.update_student_status(names[id],"Present")
        print("updated excel")
        if id+1:
            cv2.putText(
                img,
                names[id],
                (x, y - 4),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                1,
                cv2.LINE_AA,
            )
        

    cv2.imshow("Recognize", img)
    cv2.waitKey(1)

                    # if cv2.waitKey(1) & 0xFF == ord("q"):
                    #     break



    # todo: update  names with unique id and test on images with and then on video
    # 
