# region Import Packages

import sys

from BlueWhale.TextUpper.TextUpper import TextUpper

from MidWare.SelectLanguage.SelectLanguage import SelectLanguage
from MidWare.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.CreatePromt.CreatePromt import CreatePromt
from MidWare.Menus.Menus import Menus

from Utils.Languages.English import Messages as EngMessages
from Utils.Languages.Türkçe import Messages as TrMessages

from colorama import init, Fore

# endregion

init(autoreset=True)

# region UserPromt Class

class UserPromt:

    # region DocString

    """
    
    """

    # endregion

    # region Init

    def __init__(self) -> None:

        self.SelectLanguages = SelectLanguage()
        self.PrintTerminals = PrintTerminal()
        self.CreatePromts = CreatePromt()
        self.TextUppers = TextUpper()
        self.Messages = EngMessages()
        self.Menus = Menus()
        
        self.processes = self.Messages.process
        self.system = self.Messages.system
        self.menu = self.Messages.menu
        self.info = self.Messages.info
        
        self.__language = None
        
    # endregion

    # region Main

    def main(self):

        self.changeLanguage()    
        choice = self.choiceProcess()
        self.process(choice)

    # endregion
 
    # region Choice Process

    def choiceProcess(self):

        self.CreatePromts.main(self.__language, self.Menus.mainMenu, 80)

        choice = input(f"{Fore.YELLOW}{self.menu['C']['process']} ")

        return choice

    # endregion

    # region Process

    def process(self, choice):

        if choice == '1':

            self.processOne()

        elif choice == 'L' or choice == 'l':

            self.SelectLanguages.main()
            
        else:
            self.PrintTerminals.normalPrint(f"{self.system['5']['message']} ", Fore.RED)
            sys.exit()
        
        print("\n")

        status = input(f"{self.menu['D']['process']} ")

        if status == '':
            self.PrintTerminals.normalPrint(f"{self.system['5']['message']} ", Fore.RED)
        else:
            self.main()

    # endregion

    # region Process One

    def processOne(self):

        self.CreatePromts.main(self.__language, self.Menus.processOneDetail, 80)

        choice = input(f"{Fore.YELLOW}{self.menu['C']['process']} ")

        if choice == 'G' or choice == 'g':
            self.main()

        elif choice == '':
            sys.exit()

        if choice == '1':
            text = input(f"\n{self.processes['1']['message']}")
            resultText = self.TextUppers.main(1, text)

            self.PrintTerminals.normalPrint(resultText, Fore.WHITE)

        elif choice == '2':
            sourcePath = input(f"\n{self.processes['2']['message']}")
            targetPath = input(f"\n{self.processes['3']['message']}")

            result = self.TextUppers.main(2, None, sourcePath, targetPath)

            self.PrintTerminals.normalPrint(f"{self.info[str(result)]['message']} ", Fore.WHITE)

    # endregion

    # region Change Language   
     
    def changeLanguage(self):

        self.__language = SelectLanguage.language

        if self.__language == 'English':
            self.Messages = EngMessages()
        elif self.__language == 'Türkçe':
            self.Messages = TrMessages()
        else:
            self.Messages = EngMessages()
        
        self.processes = self.Messages.process
        self.system = self.Messages.system
        self.menu = self.Messages.menu
        self.info = self.Messages.info
        
    # endregion


# endregion