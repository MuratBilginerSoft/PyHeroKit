# region Import Packages

import sys

from Promt.Starter.PrintPromt.PrintPromt import PrintPromt

from MidWare.FileProcess.FileWrite.FileWrite import FileWrite

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.BrainyKit.Message.Message import Message

from MidWare.Routes.Menu.Menu import Menu

from Utils.Sessions.Sessions import Sessions

from colorama import init, Fore

init(autoreset=True)

# endregion

# region OutputMethod Class

class OutputMethod:

    # region DocString

    """
    """

    # endregion

    # region Init

    def __init__(self):

        # region Create Objects
        
        self.__pyConfigPath = 'Utils/Data/Config/PyConfig.json'

        self.PrintTerminals = PrintTerminal()  
        self.PrintPromts = PrintPromt()
        self.FileWrites = FileWrite()
        self.Messages = Message()
        self.Menus = Menu()

        # endregion
        
    # endregion

    # region Main

    def main(self):

        self.choiceProcess()
    
    # endregion

    # region Choice Process

    def choiceProcess(self):

        _, _, menu, _ = self.Messages.messageLanguage()

        self.PrintPromts.main(self.Menus.outputMethodMenu, 80)

        choice = input(f"{Fore.YELLOW}{menu['OE']['process']}")

        if choice == '1':

            self.setConfigJson('Terminal')
            Sessions.outputMethod = 'Terminal'

        elif choice == '2':

            self.setConfigJson('File')
            Sessions.outputMethod = 'File'
        
        elif choice == '':
            sys.exit()
        else:
            sys.exit()

    # endregion

    # region Set Language Json

    def setConfigJson(self, outputMethod):

        self.FileWrites.writeJson(self.__pyConfigPath, 'outputMethod', outputMethod)

    # endregion

# endregion