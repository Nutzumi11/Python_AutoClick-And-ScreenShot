import pyautogui as pg
import time

# pyautogui.position()
# Point(x=1900, y=561)
i=1
while i<=5 :
    # pg.click(1900,561)
    # path ที่เราต้องการจะเก็บภาพ
    pg.screenshot("C:\\Users\\66903\\Desktop\\python\\screenshot\\img" + str(i) + ".png")
    i+=1
    time.sleep(3)
