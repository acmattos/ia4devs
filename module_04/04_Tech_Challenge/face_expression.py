from image import detect_faces, analyze_emotions, draw_identified_box_xywh
from tqdm import tqdm

from text import create_path
from video import (cv2_video_capture, cv2_video_writer,
                   break_video_into_indexed_frames)
import cv2


def face_expression(video_in_path: str, video_out_path: str) -> None:
    """
    Perform face detection and emotion analysis on each frame of a video,
    annotate the frames, and save the result to a new video file.

    Steps
    -----
    1. Open the input video for reading.
    2. Split the video into indexed frames.
    3. Initialize a video writer for the annotated output.
    4. For each frame:
       a. Detect face bounding boxes (x, y, w, h).
       b. Analyze the emotion for each detected face.
       c. Draw a labeled rectangle around each face indicating the emotion.
       d. Write the annotated frame to the output video and display it.
       e. Allow early exit upon pressing 'q'.
    5. Release all resources when finished.

    Parameters
    ----------
    video_in_path : str
        Path to the input video file to process.
    video_out_path : str
        Path where the annotated output video will be saved.

    Returns
    -------
    None
        This function writes the processed video to disk and does not return a value.
    """
    video_capture  = cv2_video_capture(video_in_path)
    indexed_frames = break_video_into_indexed_frames(video_capture)
    writer         = cv2_video_writer(video_capture, video_out_path)

    for _, indexed_frame in tqdm(indexed_frames, desc = "Analysing video frames"):
        faces    = detect_faces(indexed_frame)
        emotions = analyze_emotions(indexed_frame, faces)

        for (x, y, w, h), emotion in zip(faces, emotions):
            draw_identified_box_xywh(indexed_frame, emotion, x, y, w, h)

        writer.write(indexed_frame)
        cv2.imshow('Face Detection', indexed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    writer.release()
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_path()

    video_in_path = "./doc/videos/tc4_video.mp4"
    video_out_path = "./doc/videos/tc4_video_fe.mp4"
    face_expression(video_in_path, video_out_path)
