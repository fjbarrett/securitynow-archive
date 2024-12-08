import os
from mutagen.mp3 import MP3

def calculate_mp3_properties(file_path):
    """
    Calculate the duration and size of an MP3 file.

    Args:
        file_path (str): Path to the MP3 file.

    Returns:
        tuple: Duration in minutes and seconds (minutes, seconds), and file size in bytes.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Get the MP3 duration
    audio = MP3(file_path)
    duration = int(audio.info.length)
    minutes = duration // 60
    seconds = duration % 60

    # Get the file size in bytes
    file_size = os.path.getsize(file_path)

    return (minutes, seconds, file_size)

if __name__ == "__main__":
    # Example usage
    file_path = input("Enter the path to your MP3 file: ").strip()
    try:
        minutes, seconds, file_size = calculate_mp3_properties(file_path)
        print(f"The duration of the MP3 file is {minutes} minutes and {seconds} seconds.")
        print(f"The size of the MP3 file is {file_size} bytes.")
    except Exception as e:
        print(f"Error: {e}")
