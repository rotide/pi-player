import os.path
import random
import sys
import subprocess
import time

PAUSE = 1

def get_playlist() -> list:
    playlist = []
    open_error = False

    try:
        with open("./playlist") as file:
            playlist = [line.rstrip() for line in file if is_file(line.rstrip())]
    except:
        open_error = True

    if len(playlist) == 0:
        if open_error:
            print(f"Error: Unable to open playlist.")
        else:
            print(f"Error: Playlist empty. Please add videos to playlist.")

    return playlist


def is_file(filepath) -> bool:
    return os.path.isfile(filepath)

def get_random_video(playlist) -> str:
    random.shuffle(playlist)
    video = playlist.pop()
    return video

def play(playlist) -> None:
    while len(playlist) > 0:
        print(f"Videos remaining in playlist: {len(playlist)}")
        video = get_random_video(playlist)
        print(f"----------")
        print(f"Playing: {video}")
        print(f"----------")
        try:
            subprocess.run(['cvlc', '--avcodec-hw=any', '--sub-track=1000', '--fullscreen', '--qt-minimal-view', '--play-and-exit', '--ignore-config', '--no-video-title', '--file-caching=10000', video], capture_output=False, text=False)
        except:
            print(f"Error: Unable to play {video}. Skipping.")

        # Pause in the event that the video storage location is unavailable (NFS share, etc).
        # This will stop the script from hammering the network share.
        time.sleep(PAUSE)

def main() -> None:
    while True:
        playlist = get_playlist()
        play(playlist)

        # Pause in the event there is an unknown error with the playlist.
        # This will stop the script from hammering the network share and the CPU.
        time.sleep(PAUSE)

if __name__ == "__main__":
    main()
