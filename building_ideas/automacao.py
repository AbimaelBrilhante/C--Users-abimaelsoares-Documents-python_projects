import pyautogui
import time
import os
import subprocess
import selenium

subprocess.call(r'C:\Program Files\Google\Chrome\Application\chrome')
time.sleep(2)
pyautogui.typewrite('https://www.gnre.pe.gov.br:444/gnre/portal/GNRE_Principal.jsp')
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.doubleClick(698,578)


print(pyautogui.position())









'''

subprocess.call(r'C:\Program Files (x86)\SAP\FrontEnd\SapGui\saplogon')
pyautogui.click(1919,1072)
time.sleep(2)
pyautogui.doubleClick(25,141)
time.sleep(5)
pyautogui.doubleClick(1279,184)
time.sleep(2)
pyautogui.typewrite('abimael s.')
time.sleep(2)
pyautogui.hotkey('tab')
time.sleep(2)
pyautogui.typewrite('Julho2022')
time.sleep(2)
pyautogui.hotkey('enter')'''