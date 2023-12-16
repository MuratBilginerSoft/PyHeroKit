# region Import Packages

import sys
from colorama import init, Fore

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.BrainyKit.Message.Message import Message
 
init(autoreset=True)

# endregion

# region ContinuePromt Class

class ContinuePromt:

    # region Init

    def __init__(self):

        # region Create Objects

        self.PrintTerminals = PrintTerminal()
        self.Messages = Message()
        
        # endregion

    # endregion
        
    # region Main
        
    def main(self, choice):

        _, system, menu, _ = self.Messages.messageLanguage()
        
        status = input(f"{menu['D']['process']} ")

        if status == 'A' or status == 'a':
            from Promt.Starter.RunPromt.RunPromt import RunPromt
            RunPromt().main()
            
        elif status == 'D' or status == 'd':
            from Promt.Starter.RunPromt.RunPromt import RunPromt
            RunPromt().run(choice)
            
        elif status == '':
            self.PrintTerminals.normalPrint(f"{system['5']['message']} ", Fore.RED)
            sys.exit()

        else:
            self.PrintTerminals.normalPrint(f"{system['5']['message']} ", Fore.RED)
            sys.exit()
              
    # endregion

# endregion                