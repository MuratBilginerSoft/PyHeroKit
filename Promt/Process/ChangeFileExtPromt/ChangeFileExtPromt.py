# region Import Packages

from colorama import init, Fore

from BlueWhale.ChangeFileExt.ChangeFileExt import ChangeFileExt

from Promt.Starter.PrintPromt.PrintPromt import PrintPromt

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.Settings.OutputMethod.OutputMethod import OutputMethod  
from MidWare.BrainyKit.Message.Message import Message

from Utils.Sessions.Sessions import Sessions


init(autoreset=True)

# endregion

# region DeleteExtFilePromt Class

class ChangeFileExtPromt:

    # region Init

    def __init__(self):

        # region Create Objects
        
        self.ChangeFileExts = ChangeFileExt()
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
        oldExtension = input(f"\n{processes['8']['message']}")
        newExtension = input(f"\n{processes['9']['message']}")
        newExtension = f".{newExtension}"
        subFolderStatus = input(f"\n{processes['10']['message']}")

        if ((subFolderStatus == 'E' or subFolderStatus == 'e') or (subFolderStatus == 'Y' or subFolderStatus == 'y')):
            subFolderStatus = True
        else:
            subFolderStatus = False

        output, result = self.ChangeFileExts.main(folderPath, oldExtension, newExtension, subFolderStatus)

        if output == 202:

            self.PrintTerminals.normalPrint(result, Fore.WHITE)

        elif output == 203:

            self.PrintTerminals.normalPrint(f"{result} - {info[str(output)]['message']} ", Fore.WHITE)
        
        else:
            self.PrintTerminals.normalPrint(f"{info[str(output)]['message']} ", Fore.WHITE)

    # endregion

# endregion                