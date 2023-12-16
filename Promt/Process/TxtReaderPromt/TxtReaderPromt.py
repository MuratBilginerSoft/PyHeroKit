# region Import Packages

from colorama import init, Fore

from BlueWhale.TxtReader.TxtReader import TxtReader

from Promt.Starter.PrintPromt.PrintPromt import PrintPromt

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.Settings.OutputMethod.OutputMethod import OutputMethod

from Utils.Sessions.Sessions import Sessions

init(autoreset=True)

# endregion

# region ReadTextFilePromt Class

class TxtReaderPromt:

    # region Init

    def __init__(self):

        # region Create Objects

        self.PrintTerminals = PrintTerminal()
        self.OutputMethods = OutputMethod()
        self.PrintPromts = PrintPromt()
        self.TxtReaders = TxtReader()

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

        sourcePath = input(f"\n{self.processes['2']['message']}")
        output, result = self.TxtReaders.main(sourcePath)

        if output == 202:

            self.PrintTerminals.normalPrint(result, Fore.WHITE)

        elif output == 203:

            self.PrintTerminals.normalPrint(f"{result} - {self.info[str(output)]['message']} ", Fore.WHITE)
        
        else:
            self.PrintTerminals.normalPrint(f"{self.info[str(output)]['message']} ", Fore.WHITE)
    
    # endregion

# endregion                