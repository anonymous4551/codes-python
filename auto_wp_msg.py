import pyautogui as pt
import time
limit = input("ENter limit : ")
msg = input("Enter msg : ")
i = 0


while i<int(limit):

    pt.typewrite(msg)
    pt.press("ENter")

    i+=1