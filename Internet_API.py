

import pyautogui
import pyperclip
from webbrowser import open_new_tab
class internet_parser:
    def __init__(self,site_link):
        self.site_link = site_link
        self.site_open = False

    def set_link(self,new_link):
        self.site_link = new_link

    def open_site(self):
        open_new_tab(self.site_link)
        self.site_open = True
    
    def close_tab(self):
        if self.site_open == True:
            pyautogui.hotkey("ctrl","w")
        else:
            print("Site Is Not Open")

    def parse_site_text(self):
        if self.site_open == True:
            pyautogui.moveTo(600,600)
            pyautogui.click()
            pyautogui.hotkey("ctrl","a")
            pyautogui.hotkey("ctrl","c")
            return pyperclip.paste()
        else:
            print("Sorry Site is Not Open!")