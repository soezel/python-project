
"""
ToDo: Welche Bibliotheken müssen eingebunden werden?
Lesen Sie hierzu IB-Selenium Webdriver

"""
import os
from selenium import webdriver                  # importiere das Modul webdriver aus dem Modul selenium 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service #importiere die Klasse Service aus selenium.webdriver.firefox.service
from selenium.webdriver.chrome.options import Options
import time

class cookieBot():

    def __init__(self):

        s = Service('./geckodriver') #Linux und Mac
        #s = Service('geckodriver.exe') #Windows

        options = Options()
        options.binary_location = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        self.browser = webdriver.Chrome(executable_path=r'/python-project/coockie-clicker/./geckodriver', options=options)
       
        # Kopieren Sie den Source Code für CookieClicker aus dem Moodle-Kurs in dieses Verzeichnis
        directory = os.path.realpath(os.path.dirname(__file__)) # diese OS-Methode gibt Dateipfad zurück
        path = 'coockie_clicker/index.html' + directory #Dateipfad zum Spiel auf Ihrem PC
        self.browser.get(path)

        """
        -- Ab hier ist die Webseite geladen --
        ToDo: Legen Sie geeignete Variablen an
        """
        success = False
        element = self.browser.find_element(By.ID,'detector-events') #sucht Webelements auf Webseite anhand ID
        element.click() #click auf das Webelement
        success = True
        return success
   
bot = cookieBot()
time.sleep(1)
while(True):
    bot.clickCookie()
