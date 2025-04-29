# Stemble Keyboard Automation Tool

This tool automates keyboard input patterns for browsers on MacOS. It can type sequences of "A" followed by "." or "," with specific patterns.

## Setup

1. Make sure you have Python 3.x installed on your system
2. Install the required dependency:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python3 keyboard_auto.py
   ```

2. When prompted:
   - Enter the number of passes you want to perform
   - Enter the delay between keystrokes (default is 0.1 seconds)

3. After starting, you'll have 5 seconds to switch to your browser window where you want the input to occur.

## Pattern Description

Each pass consists of:
1. 48 repetitions of "A" followed by "."
2. One "]" character
3. 48 repetitions of "A" followed by ","
4. One "]" character

## Safety Features

- Move your mouse to the upper-left corner of the screen to stop the script (fail-safe feature)
- Press Ctrl+C in the terminal to stop the script
- You can adjust the delay between keystrokes to ensure reliable input

## Notes

- Make sure your browser window is active when the script starts typing
- The script includes a 5-second delay at the start to give you time to switch windows
- If you need to stop the script immediately, move your mouse to the upper-left corner of the screen 