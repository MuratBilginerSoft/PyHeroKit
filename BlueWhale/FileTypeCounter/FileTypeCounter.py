# region Import Packages

from colorama import init, Fore
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


# region FileTypeCounter Class

class FileTypeCounter:

    # region DocString

    """
    """

    # endregion

    # region Init

    def __init__(self):

        self.FolderControls = FolderControl()
        self.PrintTerminals = PrintTerminal()
        self.FileControls = FileControl()
        self.FileReaders = FileReader()
        self.FileCreates = FileCreate()
        self.Messages = Message()
    # endregion

    # region Main

    def main(self, sourcePath=None):

        folderStatus = self.FolderControls.main(sourcePath)

        if folderStatus == 404:
            return 404, None
        
        elif folderStatus == 405:
            return 405, None

        else:

            _, system, _, info = self.Messages.messageLanguage()

            folderCount, fileCount, fileTypes = self.fileCounter(sourcePath)

            text = f"{'*'*30}\n\n{system['12']['message']}{folderCount}\n{system['13']['message']}{fileCount}\n{system['14']['message']}{fileTypes}\n\n{'*'*30}\n\n"
        
            if Sessions.outputMethod == 'Terminal':
        
                return 202, text
                
            elif Sessions.outputMethod == 'File':

                fileName = self.FileCreates.main(text, 'FileTypeCounter')
                return 203, fileName

            else:
                return 402, None

    # endregion
        
    def fileCounter(self, sourcePath):

        _, _, _, info = self.Messages.messageLanguage()

        folderCount = 0
        fileCount = 0
        fileTypes = {}

        self.PrintTerminals.normalPrint(f"{info['301']['message']}", Fore.WHITE)

        for _, dirs, files in os.walk(sourcePath):
            
            folderCount += len(dirs)
            fileCount += len(files)

            self.PrintTerminals.sameLinePrint(f"{info['502']['message']}{folderCount} - {info['501']['message']}{fileCount}", Fore.WHITE)

            for file in files:
                file_extension = os.path.splitext(file)[1]
                if file_extension in fileTypes:
                    fileTypes[file_extension] += 1
                else:
                    fileTypes[file_extension] = 1

        return folderCount, fileCount, fileTypes


# endregion