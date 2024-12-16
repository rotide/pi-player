import os.path
import random
import sys
import subprocess
import time

PAUSE_BETWEEN_EACH_VIDEO = 1
PAUSE_BETWEEN_PLAYLIST_REPLAYS = 1

def get_playlist() -> list:
    try:
        with open("./play.lst") as file:
            playlist = [line.rstrip() for line in file if is_file(line.rstrip())]

        if len(playlist) == 0:
            print(f"Error: No valid file paths found in playlist.")
            sys.exit(1)
        return playlist
    except:
        print(f"Error: Unable to open playlist. Exiting.")
        sys.exit(1)

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
        time.sleep(PAUSE_BETWEEN_EACH_VIDEO)

def main() -> None:
    while True:
        playlist = get_playlist()
        play(playlist)

        # Pause in the event there is an unknown error with the playlist.
        # This will stop the script from hammering the network share and the CPU.
        time.sleep(PAUSE_BETWEEN_PLAYLIST_REPLAYS)

if __name__ == "__main__":
    main()
