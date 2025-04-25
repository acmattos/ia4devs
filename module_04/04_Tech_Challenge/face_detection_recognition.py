from image import (load_image_face_encodings_and_names, bgr_2_rgb_frame,
                   load_face_locations_and_encodings, find_name,
                   draw_identified_box_ltrb)
from tqdm import tqdm

from text import create_path
from video import (cv2_video_capture, cv2_video_writer,
                   break_video_into_indexed_frames)

import cv2


def face_detection_and_recognition(
    images_path: str,
    video_in_path: str,
    video_out_path: str
) -> None:
    """
    Detects and recognizes faces in a video using pre-encoded reference images.

    Steps
    -----
    1. Load known face encodings and associated names from a folder of images.
    2. Open the input video for frame-by-frame analysis.
    3. Break the video into indexed frames for processing.
    4. Initialize a video writer to save the annotated output.
    5. For each frame:
       a. Convert BGR to RGB and detect face locations & encodings.
       b. Scale up the detected bounding boxes (if processing was done on a smaller frame).
       c. Match each face encoding against known encodings to find a name.
       d. Draw a labeled bounding box around each detected face.
       e. Write the annotated frame to the output video and display it in a window.
       f. Allow early exit on pressing 'q'.
    6. Release all resources when complete.

    Parameters
    ----------
    images_path : str
        Path to a directory containing reference images. Each image filename should
        correspond to the person's name (e.g., "alice.jpg" → "Alice").
    video_in_path : str
        Path to the input video file on which face recognition should be run.
    video_out_path : str
        Path where the annotated output video will be saved.

    Returns
    -------
    None
        This function produces an output video file and does not return a value.
    """
    (known_face_encodings,
     known_face_names) = load_image_face_encodings_and_names(images_path)
    video_capture      = cv2_video_capture(video_in_path)
    indexed_frames     = break_video_into_indexed_frames(video_capture)
    writer             = cv2_video_writer(video_capture, video_out_path)

    for _, indexed_frame in tqdm(indexed_frames, desc = "Analysing video frames"):
        face_locations, face_encodings = load_face_locations_and_encodings(
            bgr_2_rgb_frame(indexed_frame)
        )

        for (top, right, bottom, left), face_encoding \
            in tqdm(zip(face_locations, face_encodings), desc = "Analyzing frame faces"):
            left   *= 8
            top    *= 8
            right  *= 8
            bottom *= 8
            name = find_name(known_face_encodings, face_encoding, known_face_names)
            draw_identified_box_ltrb(indexed_frame, name, left, top, right, bottom)

        writer.write(indexed_frame)
        cv2.imshow('Video', indexed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    writer.release()
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_path()

    images_path = "./doc/images"
    video_in_path = "./doc/videos/tc4_video.mp4"
    video_out_path = "./doc/videos/tc4_video_fr.mp4"
    face_detection_and_recognition(images_path, video_in_path, video_out_path)
