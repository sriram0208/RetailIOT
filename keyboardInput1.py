from pynput import keyboard
import logging
logging.basicConfig(filename=("keyboard_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
 
def on_press(key):
    logging.info('Key {} pressed.'.format(key))
 
def on_release(key):
    logging.info('Key {} released.'.format(key))
    if str(key) == 'Key.esc':
        logging.info('Exiting...')
        return False
 
with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
