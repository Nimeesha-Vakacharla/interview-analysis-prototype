from deepface import DeepFace
import os

def analyze_frames(frame_folder):
    results = []

    for file in os.listdir(frame_folder):
        if file.endswith(".jpg"):
            path = os.path.join(frame_folder, file)

            try:
                res = DeepFace.analyze(
                    path,
                    actions=['emotion'],
                    enforce_detection=False
                )
                results.append(res[0]['emotion'])
            except:
                continue

    return results