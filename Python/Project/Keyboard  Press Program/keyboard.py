import keyboard

def on_key_press(event):
    print("Key Pressed" , event.name)

def on_key_release(event):
    print("Key Released" , event.name)

keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)

print("Keyboard is Waiting NOW")
keyboard.wait('esc')