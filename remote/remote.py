

import keyboard



keyboard_keys = {
    "GP1126" : "right",
    "GP1136" : "left",
}


async def execute(keycode:str):
    if keycode in list(keyboard_keys.keys()):
        hotkey = keyboard_keys[keycode]
        keyboard.press_and_release(hotkey)
        return True
    return False