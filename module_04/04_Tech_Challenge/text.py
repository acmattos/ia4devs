from pathlib import Path
from tqdm import tqdm

import speech_recognition as sr


def transcribe_sr_audio(sr_audio, text_file, use_google: bool = True) -> None:
    """
    Transcribe speech from an AudioData object and save the text to a file.

    This function uses the SpeechRecognition library to perform speech-to-text
    on an AudioData instance, either via Google’s free web API or via the Vosk
    offline recognizer. It then writes the resulting transcription to disk
    in manageable chunks, showing progress as it saves.

    Parameters
    ----------
    sr_audio : sr.AudioData
        An AudioData object containing the audio samples and sample rate,
        typically obtained via `recognizer.record(source)` on an `sr.AudioFile`.
    text_file : str
        Path (including filename) where the transcription should be saved.
        The file will be created or overwritten.
    use_google : bool, optional
        If True, use `recognize_google` (requires internet). If False,
        use `recognize_vosk` (offline, requires Vosk model installed).
        Default is True.

    Returns
    -------
    None
        Writes the transcription to `text_file` and prints it to the console.
        Does not return a value.

    Raises
    ------
    sr.RequestError
        If the Google API is unreachable or returns an error.
    sr.UnknownValueError
        If the recognizer could not understand the audio.
    Exception
        Any other errors during recognition or file I/O are propagated.

    Side Effects
    ------------
    - Prints the full transcription to stdout.
    - Displays a tqdm progress bar while writing the file in 1 KB chunks.
    """
    recognizer = sr.Recognizer()

    if use_google:
        text = recognizer.recognize_google(sr_audio, language="en-US")
    else:
        text = recognizer.recognize_vosk(sr_audio, language="en-US")
    print(f"\nTranscription: {text}\n" )

    with open(text_file, 'w', encoding='utf-8') as file:
        chunk_size = 1024  # 1KB por chunk
        text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        
        for chunk in tqdm(text_chunks, desc="Saving transcription to file"):
            file.write(chunk)

def create_path(path: str = "./doc/videos/result") -> None:
    """
    Ensure that the given directory path exists by creating any missing
    parent directories and the final directory itself.

    Parameters
    ----------
    path : str
        The directory to create (and any missing parents). E.g. "./doc/videos/result".
    """
    Path(path).mkdir(parents=True, exist_ok=True)
