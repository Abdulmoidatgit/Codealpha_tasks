import cv2
import numpy as np

from ultralytics import YOLO
from sort import Sort

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Initialize SORT tracker
tracker = Sort(
    max_age=20,
    min_hits=3,
    iou_threshold=0.3
)

# Open webcam
cap = cv2.VideoCapture(0)

# For video file use:
# cap = cv2.VideoCapture("videos/test.mp4")

while True:

    success, frame = cap.read()

    if not success:
        break

    # YOLO Detection
    results = model(frame)

    detections = np.empty((0, 5))

    for result in results:

        boxes = result.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]

            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            confidence = float(box.conf[0])

            class_id = int(box.cls[0])

            class_name = model.names[class_id]

            # Only detect confident objects
            if confidence > 0.5:

                current_detection = np.array(
                    [x1, y1, x2, y2, confidence]
                )

                detections = np.vstack(
                    (detections, current_detection)
                )

    # Object Tracking
    tracked_objects = tracker.update(detections)

    for obj in tracked_objects:

        x1, y1, x2, y2, track_id = obj

        x1, y1, x2, y2, track_id = map(
            int,
            [x1, y1, x2, y2, track_id]
        )

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Display tracking ID
        cv2.putText(
            frame,
            f"ID: {track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # Show output
    cv2.imshow(
        "Real-Time Object Detection & Tracking",
        frame
    )

    # Exit on Q key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()