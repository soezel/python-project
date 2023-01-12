from selenium import webdriver                  # importiere das Modul webdriver aus dem Modul selenium 
from selenium.webdriver.common.by import By     # importiere die Klasse By aus dem Modul by aus common aus webdriver aus selenium
from selenium.webdriver.chrome.service import Service #importiere die Klasse Service aus selenium.webdriver.firefox.service
from selenium.webdriver.chrome.options import Options

from time import sleep as schlafen_fuers_laden  # importiere die Methode sleep aus dem Modul time als
                                                # (Funktions-)Name schlafe_zum_laden in den Namespace von particle_clicker.py 


""" Klasse "ParticleBot" """
class ParticleBot():


    def __init__(self, url, timeout):
        """
        usage: Erzeuge eine particleBot- Instanz mit ParticleBot("https://...",2)
        @param url - string: Web-Url, die aufgerufen werden soll (https://...)
        @param timeout - int: Timout in Sekunden zum Laden der Webseite
        """

        options = Options()
        options.binary_location = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        self.browser = webdriver.Chrome(executable_path=r'./geckodriver', options=options)

        self.url = url
        self.browser.get(self.url) #Laden der Webseite
        self.browser.implicitly_wait(timeout) # Wartezeit des Webdrivers bis @param timout 


    def click_element(self,element_id):
        """
        usage: Findet ein Web-Element anhand seiner ID und klickt darauf.
        @param element_id: - str: HTML-ID des Elemements
        @return success: - boolean: Rückgabewert -> Erfolg, True oder False    
        """
        success = False
        element = self.browser.find_element(By.ID,'detector-events') #sucht Webelements auf Webseite anhand ID
        element.click() #click auf das Webelement
        success = True
        return success



"""
Erzeugt die Instanz der Klasse ParticleBot für die Webseite "https://particle-clicker.web.cern.ch/" 
mit einem Timeout von 2 Sekunden
"""
bot = ParticleBot("https://particle-clicker.web.cern.ch/",2) 
schlafen_fuers_laden(1) #Aufruf der Methode sleep(1) in alternativem Namensraum schlafen_fuers_laden
while(True):
    bot.click_element('detector-events') #Aufruf der Klassenmethode zum Drücken eines Webelements per ID