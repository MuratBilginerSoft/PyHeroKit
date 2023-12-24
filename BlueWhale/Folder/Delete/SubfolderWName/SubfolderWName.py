# region Import Packages

from colorama import init, Fore
import shutil
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

# region DeleteSubfolder Class

class DeleteSubfolderWithName:

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

    def main(self, sourcePath=None, folderName=None):

        effectedFolderCount = 0
        folderStatus = self.FolderControls.main(sourcePath)

        if folderStatus == 404:
            return 404, None
        
        elif folderStatus == 405:
            return 405, None

        else:

            _, system, menu, _ = self.Messages.messageLanguage()

            effectedFolderCount, folderList = self.findSubfolder(sourcePath, folderName)

            text = f"{Fore.BLUE + '*'*30 + Fore.RESET}\n\n{system['18']['message']}{folderList}\n\n{system['20']['message']}{effectedFolderCount}\n\n{Fore.BLUE + '*'*30 + Fore.RESET}\n\n"

            self.PrintTerminals.normalPrint(text, Fore.WHITE)

            decision = input(f"\n{menu['S']['process']}")

            if decision == 'E' or decision == 'e':

                deletedFolderCount, folderList = self.deleteSubfolder(sourcePath, folderName, effectedFolderCount)

                if Sessions.outputMethod == 'Terminal':

                    text = f"{Fore.BLUE + '*'*30 + Fore.RESET}\n\n{system['18']['message']}{folderList}\n\n{system['20']['message']}{deletedFolderCount}\n\n{Fore.BLUE + '*'*30 + Fore.RESET}\n\n"
            
                    return 202, text
                    
                elif Sessions.outputMethod == 'File':

                    text = f"{'*'*40}\n\n{system['18']['message']}{folderList}\n\n{system['20']['message']}{deletedFolderCount}\n\n{'*'*40}\n\n"

                    fileName = self.FileCreates.main(text, 'DeleteSubfolder')
                    return 203, fileName

                else:
                    return 402, None

            else:
                return 406, None

    # endregion

    # region Find File With Ext
                
    def findSubfolder(self, sourcePath, folderName):

        _, _, _, info = self.Messages.messageLanguage()

        self.PrintTerminals.normalPrint(f"{info['301']['message']}\n", Fore.WHITE)

        effectedFolderCount = 0
        folderList = []

        for root, dirs, files in os.walk(sourcePath, topdown=False):
            for name in dirs:
                if name == folderName:
                    folderList.append(os.path.join(root, name))
                    effectedFolderCount += 1
            
        return effectedFolderCount, folderList

    # endregion

    # region Delete File With Ext

            
    def deleteSubfolder(self, sourcePath, folderName, effectedFolderCount):
        
        _, _, _, info = self.Messages.messageLanguage()

        self.PrintTerminals.normalPrint(f"{info['301']['message']}\n", Fore.WHITE)

        deletedFolderCount = 0 
        folderList = []

        for root, dirs, files in os.walk(sourcePath, topdown=False):
            for name in dirs:
                if name == folderName:
                    deletedFolderCount += 1
                    folderList.append(os.path.join(root, name))
                    shutil.rmtree(os.path.join(root, name))
                    progress = int((deletedFolderCount / effectedFolderCount) * 100)
                    self.PrintTerminals.sameLinePrint(f"{info['302']['message']} %{progress}", Fore.WHITE)


        return deletedFolderCount, folderList

    # endregion

# endregion