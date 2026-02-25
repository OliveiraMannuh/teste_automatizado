import subprocess
import pyautogui 
import time
# -*- coding: utf-8 -*-

for i in range(3):  # repete 10 vezes
    print(f'Repetição {i+1}')

    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('home')
    time.sleep(0.5)
    pyautogui.press('down', presses=12, interval=0.1)
    time.sleep(1)

    # Clicando no votado
    time.sleep(1)
    pyautogui.click(x=843, y=725)

    # Confirmando ser humano
    time.sleep(5)
    pyautogui.click(x=829, y=345)

    # Votar novamente
    time.sleep(5)
    pyautogui.click(x=946, y=366)
    
    pyautogui.press('home')
    
    pyautogui.hotkey('alt', 'tab')
    time.sleep(5) 