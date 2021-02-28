import os
import subprocess
import ffmpeg

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    inputName = os.path.join(current_dir, "videos", "Toy - Coração não tem idade.mp4")
    outName = os.path.join(current_dir, "music", "Toy - Coração não tem idade.mp3")
    subprocess.run(['./ffmpeg.exe', '-i', inputName, outName])