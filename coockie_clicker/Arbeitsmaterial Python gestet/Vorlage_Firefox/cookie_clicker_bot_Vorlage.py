
"""
ToDo: Welche Bibliotheken müssen eingebunden werden?
Lesen Sie hierzu IB-Selenium Webdriver

"""


class cookieBot():

    def __init__(self):

        #s = Service('./geckodriver') #Linux und Mac
        s = Service('geckodriver.exe') #Windows

        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
       
        # Kopieren Sie den Source Code für CookieClicker aus dem Moodle-Kurs in dieses Verzeichnis
        directory = os.path.realpath(os.path.dirname(__file__)) # diese OS-Methode gibt Dateipfad zurück
        path = 'file://'+ directory + '/CookieClickerSource/index.html' #Dateipfad zum Spiel auf Ihrem PC
        self.browser.get(path)

        """
        -- Ab hier ist die Webseite geladen --
        ToDo: Legen Sie geeignete Variablen an
        """
   
bot = cookieBot()
time.sleep(1)
while(True):
    bot.clickCookie()
