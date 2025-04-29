import pyautogui
import time
from typing import Literal

# Safety feature: pyautogui has a fail-safe feature
# Moving mouse to upper-left corner will stop the script
pyautogui.FAILSAFE = True

def type_pattern(num_passes: int, delay: float = 0.1):
    """
    Types the specified pattern for the given number of passes.
    Each pass consists of:
    1. 48 'A' + '.' followed by ']'
    2. 48 'A' + ',' followed by ']'
    
    Args:
        num_passes: Number of times to repeat the entire pattern
        delay: Delay between each keystroke in seconds
    """
    # Give user time to switch to the correct window
    print("Starting in 5 seconds... Switch to your target window!")
    time.sleep(5)
    
    try:
        for pass_num in range(num_passes):
            print(f"Pass {pass_num + 1}/{num_passes}")
            
            # First pattern: A. x 48 followed by ]
            for _ in range(48):
                pyautogui.write('A', interval=delay)
                pyautogui.write('.', interval=delay)
            pyautogui.write(']', interval=delay)
            
            # Second pattern: A, x 48 followed by ]
            for _ in range(48):
                pyautogui.write('A', interval=delay)
                pyautogui.write(',', interval=delay)
            pyautogui.write(']', interval=delay)
            
            print(f"Completed pass {pass_num + 1}")
            
    except pyautogui.FailSafeException:
        print("\nFail-safe triggered! Script stopped.")
    except KeyboardInterrupt:
        print("\nScript manually interrupted!")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    print("Keyboard Automation Tool")
    print("------------------------")
    print("NOTE: Move mouse to upper-left corner to stop the script")
    
    while True:
        try:
            passes = int(input("Enter number of passes to perform (or 0 to exit): "))
            if passes == 0:
                break
            
            delay = float(input("Enter delay between keystrokes in seconds (default 0.1): ") or 0.1)
            
            type_pattern(passes, delay)
            
        except ValueError:
            print("Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\nExiting...")
            break 