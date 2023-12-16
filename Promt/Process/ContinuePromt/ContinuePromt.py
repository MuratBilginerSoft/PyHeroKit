# region Import Packages

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
        
    def main(self):

        _, system, menu, _ = self.Messages.messageLanguage()
        
        print("\n")

        status = input(f"{menu['D']['process']} ")

        if status == '':
            self.PrintTerminals.normalPrint(f"{system['5']['message']} ", Fore.RED)
        else:
            from Promt.Starter.RunPromt.RunPromt import RunPromt
            RunPromt().main()
            
    # endregion

# endregion                