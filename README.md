# Face Detection & Recognition

This project uses OpenCV and Python to perform real-time face detection and recognition using your webcam or images. It is designed for easy training, recognition, and extension.

## Features
- Detect faces in images and video streams
- Recognize known faces using a trained model
- Real-time webcam recognition with UI enhancements
- Easy to add new faces to the dataset
- Confidence score display for recognition

## Folder Structure
```
face_detection_And_recognizer/
  faces/           # Training images, one folder per person
  src/             # Source code and model files
    detect_face.py
    face_recog.py
    recognizer.py
    video.py
    ...
```

## Setup
1. **Install dependencies:**
   ```bash
   pip install opencv-python opencv-contrib-python numpy
   ```
2. **Add training images:**
   - Place images of each person in a separate folder under `faces/` (e.g., `faces/John/`, `faces/Jane/`).

## Usage
1. **Train the model:**
   ```bash
   cd src
   python face_recog.py
   ```
2. **Real-time recognition (webcam):**
   ```bash
   python video.py
   ```
   - Press `d` to exit the webcam window.
3. **Recognize faces in a single frame:**
   ```bash
   python recognizer.py
   ```
4. **Detect faces in a static image:**
   ```bash
   python detect_face.py
   ```

## Customization
- To add new people, just add their images to a new folder in `faces/` and retrain the model.
- The UI and recognition logic can be easily extended in `src/video.py`.

## Credits
- Built with [OpenCV](https://opencv.org/) and Python.
- Inspired by open-source face recognition tutorials.

---
For more details, see the code in the [src folder](https://github.com/lakhveer-singh7/opencv-projects/tree/main/face_detection_And_recognizer/src). 