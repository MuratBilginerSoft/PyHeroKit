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

# region DeleteExtFile Class

class DeleteExtFile:

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

    def main(self, sourcePath=None, extension=None):

        effectedFileCount = 0
        folderStatus = self.FolderControls.main(sourcePath)

        if folderStatus == 404:
            return 404, None
        
        elif folderStatus == 405:
            return 405, None

        else:

            _, system, menu, _ = self.Messages.messageLanguage()

            effectedFileCount, fileList = self.findFileWithExt(sourcePath, extension)

            text = f"{Fore.BLUE + '*'*30 + Fore.RESET}\n\n{system['17']['message']}{fileList}\n\n{system['13']['message']}{effectedFileCount}\n\n{Fore.BLUE + '*'*30 + Fore.RESET}\n\n"

            self.PrintTerminals.normalPrint(text, Fore.WHITE)

            decision = input(f"\n{menu['S']['process']}")

            if decision == 'E' or decision == 'e':

                deletedFileCount, fileList = self.deleteFileWithExt(sourcePath, extension, effectedFileCount)

                if Sessions.outputMethod == 'Terminal':

                    text = f"{Fore.BLUE + '*'*30 + Fore.RESET}\n\n{system['16']['message']}{fileList}\n\n{system['13']['message']}{deletedFileCount}\n\n{Fore.BLUE + '*'*30 + Fore.RESET}\n\n"
            
                    return 202, text
                    
                elif Sessions.outputMethod == 'File':

                    text = f"{'*'*100}\n\n{system['16']['message']}{fileList}\n\n{system['13']['message']}{deletedFileCount}\n\n{'*'*100}\n\n"

                    fileName = self.FileCreates.main(text, 'DeleteExtFile')
                    return 203, fileName

                else:
                    return 402, None

            else:
                return 406, None

    # endregion

    # region Find File With Ext
                
    def findFileWithExt(self, sourcePath, extension):

        _, _, _, info = self.Messages.messageLanguage()

        self.PrintTerminals.normalPrint(f"{info['301']['message']}\n", Fore.WHITE)

        effectedFileCount = 0
        fileList = []  

        files = glob.glob(f"{sourcePath}/**/*.{extension}", recursive=True)

        for file in files:
            effectedFileCount += 1
            filename = os.path.basename(file)
            fileList.append(filename)
            
        return effectedFileCount, fileList

    # endregion

    # region Delete File With Ext
        
    def deleteFileWithExt(self, sourcePath, extension, effectedFileCount):

        _, _, _, info = self.Messages.messageLanguage()

        self.PrintTerminals.normalPrint(f"{info['301']['message']}\n", Fore.WHITE)

        deleteFileCount = 0
        fileList = []  

        files = glob.glob(f"{sourcePath}/**/*.{extension}", recursive=True)

        for file in files:
            deleteFileCount += 1
            filename = os.path.basename(file)
            fileList.append(filename)
            os.remove(file)
            progress = int((deleteFileCount / effectedFileCount) * 100)
            self.PrintTerminals.sameLinePrint(f"{info['302']['message']} %{progress}", Fore.WHITE)

        return deleteFileCount, fileList

    # endregion

# endregion