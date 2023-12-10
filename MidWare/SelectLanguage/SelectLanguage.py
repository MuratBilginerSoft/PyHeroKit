# region Import Packages
import json
import sys

from MidWare.PrintTerminal.PrintTerminal import PrintTerminal
from Utils.Languages.English import Messages as EngMessages
from Utils.Languages.Türkçe import Messages as TrMessages

from MidWare.Menus.Menus import Menus
from MidWare.CreatePromt.CreatePromt import CreatePromt

from colorama import init, Fore

# endregion

init(autoreset=True)

# region SelectLanguage Class

class SelectLanguage:

    # region DocString

    """

    This module, SelectLanguage, is responsible for handling the language selection in the application.

    It provides two main functions:

        - `load_language_from_file`: This function reads the current language setting from a configuration file.
        - `change_language`: This function changes the current language setting and saves it to the configuration file.

    Usage:
        import SelectLanguage
        language = SelectLanguage.main()
        SelectLanguage.setLanguageJson("Türkçe")

    """

    # endregion

    # region Class Variables

    language = None

    # endregion

    # region Init

    def __init__(self):
        
        self.__pyConfigPath = 'Utils/Config/PyConfig.json'
        self.__language = "English"

        self.PrintTerminals = PrintTerminal()  
        self.CreatePromts = CreatePromt()
        self.Messages = EngMessages()
        self.Menus = Menus()
        
        self.processes = self.Messages.process
        self.system = self.Messages.system
        self.menu = self.Messages.menu
        self.info = self.Messages.info

    # endregion

    # region Main

    def main(self):

        self.selectLanguage()
        self.choiceProcess(self.__language)
    
    # endregion

    # region Select Language

    def selectLanguage(self):

        if SelectLanguage.language == 'English':
            self.Messages = EngMessages()
            self.__endMessage = "Invalid choice..."
            self.__language = "English"
        elif SelectLanguage.language == 'Türkçe':
            self.Messages = TrMessages()
            self.__endMessage = "Geçersiz seçim..."
            self.__language = "Türkçe"
        else:
            self.Messages = EngMessages()
            self.__endMessage = "Invalid choice..."
            self.__language = "English"    
        
        self.processes = self.Messages.process
        self.system = self.Messages.system
        self.menu = self.Messages.menu
        self.info = self.Messages.info

    # endregion

    # region Choice Process

    def choiceProcess(self, language="English"):

        self.CreatePromts.main(language, self.Menus.languageMenu, 80)

        choice = input(f"{Fore.YELLOW}{self.menu['LE']['process']}")

        if choice == '1':

            self.setLanguageJson('English')

        elif choice == '2':

            self.setLanguageJson('Türkçe')
        
        elif choice == '':
            sys.exit()
        else:
            print(self.__endMessage)


    # endregion

    # region Set Language Json

    def setLanguageJson(self, language):

        with open(self.__pyConfigPath, 'r+', encoding='utf-8') as f:
            
            data = json.load(f)
            data['language'] = language  
            f.seek(0) 
            json.dump(data, f, indent=4, ensure_ascii=False)  
            f.truncate()
        
        SelectLanguage.language = language
        print(SelectLanguage.language)
    
    # endregion

# endregion