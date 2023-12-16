# region Import Packages

from colorama import init, Fore

from BlueWhale.FileTypeCounter.FileTypeCounter import FileTypeCounter

from Promt.Starter.PrintPromt.PrintPromt import PrintPromt

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.Settings.OutputMethod.OutputMethod import OutputMethod  
from MidWare.BrainyKit.Message.Message import Message

from Utils.Sessions.Sessions import Sessions


init(autoreset=True)

# endregion

# region FileTypeCounterPromt Class

class FileTypeCounterPromt:

    # region Init

    def __init__(self):

        # region Create Objects
        
        self.FileTypeCounters = FileTypeCounter()
        self.PrintTerminals = PrintTerminal()
        self.OutputMethods = OutputMethod()
        self.PrintPromts = PrintPromt()
        self.Messages = Message()
        
        # endregion

    # endregion
        
    # region Main
        
    def main(self):

        processes, _, _, info = self.Messages.messageLanguage()

        folderPath = input(f"\n{processes['5']['message']}")

        output, result = self.FileTypeCounters.main(folderPath)

        if output == 202:

            self.PrintTerminals.normalPrint(result, Fore.WHITE)

        elif output == 203:

            self.PrintTerminals.normalPrint(f"{result} - {info[str(output)]['message']} ", Fore.WHITE)
        
        else:
            self.PrintTerminals.normalPrint(f"{info[str(output)]['message']} ", Fore.WHITE)

    # endregion

# endregion                