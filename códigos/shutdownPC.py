import pyautogui
from time import sleep

pyautogui.press('win')
sleep(0.5)
pyautogui.write('cmd')
sleep(0.5)
pyautogui.press('enter')
sleep(1)
pyautogui.write('shutdown now')
sleep(0.5)
pyautogui.press('enter')


