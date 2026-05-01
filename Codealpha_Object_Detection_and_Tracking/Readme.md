# Real-Time Object Detection & Tracking System

An AI-powered Computer Vision project developed using **Python, OpenCV, YOLOv8, and SORT Tracking Algorithm** for real-time object detection and tracking.

This project was developed during my **Python AI Internship at @CodeAlpha**.

---

# 🚀 Features

* Real-time object detection
* Real-time object tracking
* Unique tracking IDs
* Webcam support
* Video file support
* Bounding box visualization
* Lightweight and fast YOLOv8 model
* Multiple object detection and tracking

---

# 🧠 Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Main programming language      |
| OpenCV     | Video capturing and processing |
| YOLOv8     | Object detection               |
| SORT       | Object tracking                |
| NumPy      | Numerical operations           |

---

# 📁 Project Structure

```plaintext
object_detection_tracking/
│
├── main.py
├── sort.py
├── requirements.txt
└── videos/
    └── test.mp4
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/object-detection-tracking.git
```

---

## 2️⃣ Open Project Folder

```bash
cd object-detection-tracking
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

## Webcam Mode

```python
cap = cv2.VideoCapture(0)
```

Run:

```bash
python main.py
```

---

## Video File Mode

Place your video inside:

```plaintext
videos/
```

Example:

```plaintext
videos/test.mp4
```

Replace:

```python
cap = cv2.VideoCapture(0)
```

with:

```python
cap = cv2.VideoCapture("videos/test.mp4")
```

Then run:

```bash
python main.py
```

---

# 🔥 How It Works

## 1. Video Capture

OpenCV captures frames from webcam or video.

## 2. Object Detection

YOLOv8 detects objects such as:

* Person
* Car
* Bicycle
* Dog
* Mobile phone
* etc.

## 3. Bounding Boxes

Detected objects are highlighted using rectangles.

## 4. Object Tracking

SORT tracking algorithm assigns unique IDs to objects and tracks them across frames.

---

# 📸 Example Output

```plaintext
Person -> ID 1
Car -> ID 2
Dog -> ID 3
```

with live bounding boxes and tracking IDs.

---

# 🧠 AI Concepts Used

* Computer Vision
* Deep Learning
* Convolutional Neural Networks (CNN)
* Real-Time Video Processing
* Object Detection
* Object Tracking

---

# 📦 Requirements

```txt
opencv-python
ultralytics
filterpy
scikit-image
numpy
lap
```

---

# 🎓 Internship Project

This project was developed as part of my:

> Python AI Internship at @CodeAlpha

It helped me gain practical experience in:

* AI Development
* Computer Vision
* Real-time Object Tracking
* Deep Learning Models
* OpenCV Applications

---

# 🚀 Future Improvements

* Deep SORT integration
* Face recognition
* Vehicle counting system
* Traffic monitoring
* Speed estimation
* GUI dashboard
* Flask web deployment
* GPU acceleration

---

# 👨‍💻 Author

AbdulMoeed
Computer Science Student | AI & Python Enthusiast

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!
