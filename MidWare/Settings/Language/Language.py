# region Import Packages

import sys

from Promt.Starter.PrintPromt.PrintPromt import PrintPromt

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.FileProcess.FileWrite.FileWrite import FileWrite
from MidWare.BrainyKit.Message.Message import Message
from MidWare.Routes.Menu.Menu import Menu

from Utils.Sessions.Sessions import Sessions

from colorama import init, Fore

init(autoreset=True)

# endregion

# region Language Class

class Language:

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

    # region Init

    def __init__(self):
        
        # region Create Objects
    
        self.PrintTerminals = PrintTerminal()  
        self.PrintPromts = PrintPromt()
        self.FileWrites = FileWrite()
        self.Messages = Message()
        self.Menus = Menu()

        # endregion

        # region Variables

        self.__pyConfigPath = 'Utils/Data/Config/PyConfig.json'

        # endregion

    # endregion

    # region Main

    def main(self):

        self.choiceProcess()
        self.Messages.main()
    
    # endregion

    # region Choice Process

    def choiceProcess(self):

        _, _, menu, _ = self.Messages.messageLanguage()

        self.PrintPromts.main(self.Menus.languageMenu, 80)
        choice = input(f"{Fore.YELLOW}{menu['LE']['process']}")

        if choice == '1':

            self.setLanguageJson('English')
            
        elif choice == '2':

            self.setLanguageJson('Türkçe')
            
        elif choice == '':
            sys.exit()
        else:
            sys.exit()

    # endregion

    # region Set Language Json

    def setLanguageJson(self, language):

        self.FileWrites.writeJson(self.__pyConfigPath, 'language', language)
        
        Sessions.language = language
    
    # endregion
        
# endregion