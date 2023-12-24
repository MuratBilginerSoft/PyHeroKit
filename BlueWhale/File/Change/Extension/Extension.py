# region Import Packages

from colorama import init, Fore
import glob
import os

from MidWare.FileProcess.FileControl.FileControl import FileControl
from MidWare.FileProcess.FileReader.FileReader import FileReader
from MidWare.FileProcess.FileCreate.FileCreate import FileCreate

from MidWare.FolderProcess.FolderControl.FolderControl import FolderControl

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal

from MidWare.BrainyKit.Message.Message import Message

from Utils.Sessions.Sessions import Sessions

init(autoreset=True)

# endregion

# region ChangeFileExtension Class

class ChangeFileExtension:

    # region DocString

    """
    """

    # endregion

    # region Init

    def __init__(self):

        # region Create Objects

        self.FolderControls = FolderControl()
        self.PrintTerminals = PrintTerminal()
        self.FileControls = FileControl()
        self.FileReaders = FileReader()
        self.FileCreates = FileCreate()
        self.Messages = Message()

        # endregion

    # endregion

    # region Main

    def main(self, sourcePath, oldExtension, newExtension, subFolderStatus=False):

        effectedFileCount = 0
        folderStatus = self.FolderControls.main(sourcePath)

        if folderStatus == 404:
            return 404, None
        
        elif folderStatus == 405:
            return 405, None

        else:

            _, system, menu, _ = self.Messages.messageLanguage()

            effectedFileCount, fileList, files = self.findFileWithExt(sourcePath, oldExtension, subFolderStatus)

            text = f"{Fore.BLUE + '*'*30 + Fore.RESET}\n\n{system['21']['message']}{fileList}\n\n{system['13']['message']}{effectedFileCount}\n\n{Fore.BLUE + '*'*30 + Fore.RESET}\n\n"

            self.PrintTerminals.normalPrint(text, Fore.WHITE)

            decision = input(f"\n{menu['S']['process']}")

            if decision == 'E' or decision == 'e':

                changeFileCount = self.changeFileWithExt(files, newExtension, effectedFileCount)

                if Sessions.outputMethod == 'Terminal':

                    text = f"{Fore.BLUE + '*'*30 + Fore.RESET}\n\n{system['22']['message']}{fileList}\n\n{system['13']['message']}{changeFileCount}\n\n{Fore.BLUE + '*'*30 + Fore.RESET}\n\n"
            
                    return 202, text
                    
                elif Sessions.outputMethod == 'File':

                    text = f"{'*'*40}\n\n{system['22']['message']}{fileList}\n\n{system['13']['message']}{changeFileCount}\n\n{'*'*40}\n\n"

                    fileName = self.FileCreates.main(text, 'ChangeFileExt')
                    return 203, fileName

                else:
                    return 402, None

            else:
                return 406, None

    # endregion
            
    # region Find File With Ext
                
    def findFileWithExt(self, sourcePath, oldExtension, subFolderStatus):

        _, _, _, info = self.Messages.messageLanguage()

        self.PrintTerminals.normalPrint(f"{info['301']['message']}\n", Fore.WHITE)

        effectedFileCount = 0
        fileList = []  

        if subFolderStatus == True:

            files = glob.glob(f"{sourcePath}/**/*.{oldExtension}", recursive=True)
        
        else:
            files = glob.glob(f"{sourcePath}/*.{oldExtension}")


        for file in files:
            effectedFileCount += 1
            filename = os.path.basename(file)
            fileList.append(filename)
            
        return effectedFileCount, fileList, files

    # endregion

    # region Change File Ext
        
    def changeFileWithExt(self, files, newExtension, effectedFileCount):

        _, _, _, info = self.Messages.messageLanguage()

        self.PrintTerminals.normalPrint(f"{info['301']['message']}\n", Fore.WHITE)

        changeFileCount = 0

        for file in files:

            changeFileCount += 1

            base = os.path.splitext(file)[0]
            os.rename(file, base + newExtension)

            progress = int((changeFileCount / effectedFileCount) * 100)
            self.PrintTerminals.sameLinePrint(f"{info['302']['message']} %{progress}", Fore.WHITE)

        return changeFileCount

    # endregion

# endregion