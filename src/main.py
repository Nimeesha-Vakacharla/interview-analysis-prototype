from extract_frames import extract_frames
from emotion_analysis import analyze_frames
from aggregator import aggregate_emotions
from behavior_analysis import analyze_behavior
from ollama_inference import run_ollama_analysis

VIDEO_PATH = "C:/Users/nimee/Downloads/ChaLearn2016_tiny/ChaLearn2016_tiny/train/83cmR2fkyy8.005.mp4"
FRAMES_PATH = "./frames"

# Step 1: Extract frames
extract_frames(VIDEO_PATH, FRAMES_PATH, fps=0.5)

# Step 2: Emotion analysis (DeepFace)
emotions = analyze_frames(FRAMES_PATH)

# Step 3: Aggregate emotions
emotion_stats = aggregate_emotions(emotions)

# Step 4: Behavioral analysis (MediaPipe)
behavior_stats = analyze_behavior(FRAMES_PATH)

# Step 5: Combine everything
combined_stats = {
    "emotion_summary": emotion_stats,
    "behavior_summary": behavior_stats
}

# Step 6: LLM reasoning
report = run_ollama_analysis(combined_stats)

print("\n========== FINAL REPORT ==========\n")
print(report)