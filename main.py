from pynput import keyboard, mouse


def on_click(x, y, button, pressed):
    if pressed:
        print('{}'.format((x, y)))


def on_press(key):
    if key == keyboard.Key.f12:
        print('==============================================')
        print('listener stop')
        return False
    return True


def start_listener():
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    start_listener()
