import cv2
import numpy as np

def analyze_behavior(video_path=0):
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    movement_score = 0

    prev_gray = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is not None:
            diff = cv2.absdiff(prev_gray, gray)
            movement = np.sum(diff) / diff.size
            movement_score += movement

        prev_gray = gray
        frame_count += 1

        if frame_count > 100:  # limit for testing
            break

    cap.release()

    if frame_count == 0:
        return {"Confidence": 5, "Nervousness": 5, "Presentability": 5}

    avg_movement = movement_score / frame_count

    # Simple heuristic scoring
    confidence = max(1, min(10, int(10 - avg_movement * 50)))
    nervousness = max(1, min(10, int(avg_movement * 50)))
    presentability = 6  # placeholder

    return {
        "Confidence": confidence,
        "Nervousness": nervousness,
        "Presentability": presentability
    }