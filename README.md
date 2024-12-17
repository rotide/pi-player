# pi-player
This script will:
- Play local videos from the command line utilizing CVLC (command line VLC).
- Shuffle and play video files in a playlist.
- When complete, start playing the playlist again using a new random shuffle.

## Why
I wanted to
- Play videos like old cable/antenna TV.
- Turn it on, just watch without making choices.

## Hardware
Raspberry Pi 3b+ (or newer)

## OS
Raspberry Pi OS (64-bit) Debian Bookworm w/ Raspberry Pi Desktop

## Raspberry Pi Setup Steps
1. Flash SD Card w/ OS
2. Update Pi:
   - Command: `sudo apt update && sudo apt upgrade -y`
4. Update raspi-config:
   - Command: `sudo raspi-config`
   - Set to boot to Command Line: System Options -> Boot/Auto Login -> B1 Console
   - Set HDMI Audio Out: System Options -> Audio -> vc4-hdmi
5. Set Volume
   - Command: `alsamixer`
   - Hit UP/DOWN arrow on keyboard to set desired volume

## Setup pi-player
1. Copy `pi-player.py` to whatever directory you choose
2. Create a `play.lst` file in the same directory
3. Edit `play.lst` to contain the full file paths of any videos you want the script to play

## Running pi-player
1. Login to Raspberry Pi either locally or via SSH
2. Browse to where you saved `pi-player.py`
3. Execute pi-player: `python pi-player.py`

## Tips
- If you want to run pi-player in the background without needing to stay logged in: `nohup python pi-player.py &`
- If you want to also be able to view the scripts output (prints) in the nohup file: `nohup python -u pi-player.py &`
