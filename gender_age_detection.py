import cv2
import numpy as np

# Load models
face_proto = "models/deploy.prototxt"
face_model = "models/res10_300x300_ssd_iter_140000_fp16.caffemodel"
age_proto = "models/age_deploy.prototxt"
age_model = "models/age_net.caffemodel"
gender_proto = "models/gender_deploy.prototxt"
gender_model = "models/gender_net.caffemodel"

# Load the models
face_net = cv2.dnn.readNet(face_model, face_proto)
age_net = cv2.dnn.readNet(age_model, age_proto)
gender_net = cv2.dnn.readNet(gender_model, gender_proto)

# Define model parameters
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
age_list = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(21-30)", "(31-40)", "(41-50)", "(51-60)", "(60+)"]
gender_list = ["Male", "Female"]

# Load input image
video = cv2.VideoCapture(0)  # 0 for webcam or replace with video file path

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Prepare the frame for face detection
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], swapRB=False)
    face_net.setInput(blob)
    detections = face_net.forward()

    # Loop through detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.7:  # Confidence threshold
            box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")

            # Extract face
            face = frame[startY:endY, startX:endX]
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

            # Predict gender
            gender_net.setInput(blob)
            gender_preds = gender_net.forward()
            gender = gender_list[gender_preds[0].argmax()]

            # Predict age
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age = age_list[age_preds[0].argmax()]

            # Display predictions
            label = f"{gender}, {age}"
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Show the output
    cv2.imshow("Gender and Age Detection", frame)

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
