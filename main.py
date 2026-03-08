import cv2

# Load cascade classifiers
face_ref = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_ref = cv2.CascadeClassifier("smile_ref.xml")

camera = cv2.VideoCapture(0)

def smile_detection(gray_face, face_region):
    x, y, w, h = face_region
    roi_gray = gray_face[y:y+h, x:x+w]
    smiles = smile_ref.detectMultiScale(
        roi_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(25, 25)
    )
    return smiles

def drawer_box(frame):
    # Fix: BGR2GRAY bukan RGB2GRAY
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_ref.detectMultiScale(
        optimized_frame,
        scaleFactor=1.1,
        minNeighbors=5,   # tambah ini
        minSize=(80, 80)  # fix: dari 300 jadi 80
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

        smiles = smile_detection(optimized_frame, (x, y, w, h))
        for sx, sy, sw, sh in smiles:
            cv2.rectangle(frame, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 255, 0), 2)
            cv2.putText(frame, "Smile :)", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

def close_window():
    camera.release()
    cv2.destroyAllWindows()
    exit()

# Main loop
while True:
    ret, frame = camera.read()
    if not ret:
        break

    drawer_box(frame)
    cv2.imshow("Smile Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        close_window()