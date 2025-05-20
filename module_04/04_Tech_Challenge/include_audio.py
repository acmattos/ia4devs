import os
from moviepy import VideoFileClip

def restore_audio_from_video(source_video, output_path):
    temp_output_path = ""
    if output_path.endswith('.mp4'):
        temp_output_path = output_path.replace('.mp4', '_temp.mp4')
        os.rename(output_path, temp_output_path)

    source_video = VideoFileClip(source_video)
    source_audio = source_video.audio

    video_to_recovery = VideoFileClip(temp_output_path)

    output_video = video_to_recovery.with_audio(source_audio)

    output_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    if temp_output_path and os.path.exists(temp_output_path):
        os.remove(temp_output_path)
