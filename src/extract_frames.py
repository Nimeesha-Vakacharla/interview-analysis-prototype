import cv2
import os

def extract_frames(video_path, output_folder, fps=1):
    os.makedirs(output_folder, exist_ok=True)

    # Clear old frames
    for f in os.listdir(output_folder):
        os.remove(os.path.join(output_folder, f))

    cap = cv2.VideoCapture(video_path)

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(video_fps / fps) if video_fps > 0 else 1

    count, frame_id = 0, 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % interval == 0:
            cv2.imwrite(f"{output_folder}/frame_{frame_id}.jpg", frame)
            frame_id += 1

        count += 1

    cap.release()