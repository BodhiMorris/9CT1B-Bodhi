import time
from pynput import keyboard
import threading

# Initialize the keyboard controller
keyboard_controller = keyboard.Controller()

# Variable to control the loop
running = True

def on_press(key):
    global running
    try:
        # Check if F5 is pressed
        if key == keyboard.Key.f5:
            running = False
            print("F5 pressed. Stopping the program.")
            return False  # Stop the listener
    except AttributeError:
        pass

def start_key_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Start the key listener in a separate thread
listener_thread = threading.Thread(target=start_key_listener)
listener_thread.start()

try:
    while running:
        # Press and release the 'e' key
        keyboard_controller.press('e')
        keyboard_controller.release('e')
        # Wait for one second
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated by user")

# Wait for the listener thread to finish
listener_thread.join()

print("Script finished")
eeeee