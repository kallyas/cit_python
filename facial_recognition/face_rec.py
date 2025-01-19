import cv2
from typing import Tuple


def initialize_camera(camera_index: int = 0) -> cv2.VideoCapture:
    """
    Initializes the camera for video capture.

    Args:
        camera_index (int): The index of the camera to use (default is 0).

    Returns:
        cv2.VideoCapture: The video capture object.
    """
    return cv2.VideoCapture(camera_index)


def load_face_cascade(cascade_path: str = "haarcascade_frontalface_default.xml") -> cv2.CascadeClassifier:
    """
    Loads the Haar cascade for face detection.

    Args:
        cascade_path (str): The path to the Haar cascade file (default is "haarcascade_frontalface_default.xml").

    Returns:
        cv2.CascadeClassifier: The face cascade classifier.
    """
    return cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)


def detect_faces(face_cascade: cv2.CascadeClassifier, gray_frame: cv2.Mat) -> Tuple[int, int, int, int]:
    """
    Detects faces in a grayscale frame.

    Args:
        face_cascade (cv2.CascadeClassifier): The face cascade classifier.
        gray_frame (cv2.Mat): The grayscale frame.

    Returns:
        Tuple[int, int, int, int]: The coordinates of the detected faces (x, y, width, height).
    """
    return face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)


def draw_faces(frame: cv2.Mat, faces: Tuple[int, int, int, int]) -> None:
    """
    Draws rectangles around detected faces in the frame.

    Args:
        frame (cv2.Mat): The frame to draw on.
        faces (Tuple[int, int, int, int]): The coordinates of the detected faces (x, y, width, height).
    """
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


def facial_recognition() -> None:
    """
    Performs facial recognition using the webcam feed.
    """
    cap = initialize_camera()
    face_cascade = load_face_cascade()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(face_cascade, gray)
        draw_faces(frame, faces)

        cv2.imshow("Facial Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    facial_recognition()
