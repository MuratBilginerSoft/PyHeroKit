# region Import Packages

from colorama import init, Fore

from BlueWhale.Text.AllLetterUpper.AllLetterUpper import AllLetterUpper

from Promt.Starter.PrintPromt.PrintPromt import PrintPromt

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.Settings.OutputMethod.OutputMethod import OutputMethod
from MidWare.Routes.Menu.Menu import Menu
from MidWare.Routes.Exit.Exit import Exit  

from Utils.Sessions.Sessions import Sessions


init(autoreset=True)

# endregion

# region TextUpperPromt Class

class TextUpperPromt:

    # region Init

    def __init__(self):

        # region Create Objects

        self.AllLetterUppers = AllLetterUpper()
        self.PrintTerminals = PrintTerminal()
        self.OutputMethods = OutputMethod()
        self.PrintPromts = PrintPromt()
        self.Menus = Menu()
        self.Exits = Exit()

        # endregion

        # region Variables

        self.processes = Sessions.processes 
        self.system = Sessions.system
        self.menu = Sessions.menu
        self.info = Sessions.info
    
        # endregion
    
    # endregion
        
    # region Main
        
    def main(self):

        self.PrintPromts.main(self.Menus.processOneDetail, 80)
        choice = input(f"{Fore.YELLOW}{self.menu['C']['process']} ")

        self.Exits.main(choice)

        if choice == '1':

            text = input(f"\n{self.processes['1']['message']}")
            output, result = self.AllLetterUppers.main(1, text)

            if output == 202:

                self.PrintTerminals.normalPrint(result, Fore.WHITE)

            elif output == 203:

                self.PrintTerminals.normalPrint(f"{result} - {self.info[str(output)]['message']} ", Fore.WHITE)
        
            else:
                self.PrintTerminals.normalPrint(f"{self.info[str(output)]['message']} ", Fore.WHITE)

        elif choice == '2':

            sourcePath = input(f"\n{self.processes['2']['message']}")
            targetPath = input(f"\n{self.processes['3']['message']}")

            output, result = self.AllLetterUppers.main(2, None, sourcePath, targetPath)

            if output == 203:

                self.PrintTerminals.normalPrint(f"{result} - {self.info[str(output)]['message']} ", Fore.WHITE)
        
            else:

                self.PrintTerminals.normalPrint(f"{self.info[str(output)]['message']} ", Fore.WHITE)
    
    # endregion

# endregion                