# region Import Packages

import os

from MidWare.FileProcess.FileControl.FileControl import FileControl
from MidWare.FileProcess.FileReader.FileReader import FileReader
from MidWare.FileProcess.FileCreate.FileCreate import FileCreate

# endregion

from Utils.Sessions.Sessions import Sessions

# region TextUpper Class

class AllLetterUpper:

    # region DocString

    """
    """

    # endregion

    # region Init

    def __init__(self):

        self.FileControls = FileControl()
        self.FileReaders = FileReader()
        self.FileCreates = FileCreate()
        
        self.__outputMethod = Sessions.outputMethod

    # endregion

    # region Main

    def main(self, choice=0, text=None, sourcePath=None, targetPath=None):
        
        if choice == 1:

            if self.__outputMethod == 'Terminal':
    
                result = self.stringTextUpper(text)
                return 202, result
            
            elif self.__outputMethod == 'File':

                resultText = self.stringTextUpper(text)
                fileName = self.FileCreates.main(resultText, 'TextUpper')
                return 203, fileName

            else:
                return 402, None
                
        elif choice == 2:
            return self.fileTextUpper(sourcePath, targetPath)
        
        else:
            return 402, None

    # endregion

    # region String Text Upper

    def stringTextUpper(self, text): 
        return self.turkishUpper(text)

    # endregion

    # region File Text Upper

    def fileTextUpper(self, sourcePath, targetPath):

        fileStatus, extensionStatus = self.FileControls.main(sourcePath, '.txt')

        if fileStatus == 303:
            return 403, None
        if extensionStatus == 304:
            return 401, None
        
        text = None
        text = self.FileReaders.txtRead(sourcePath)

        try:
        
            resultText = self.turkishUpper(text)
            self.FileCreates.writeFile(targetPath, resultText)
            filename = os.path.basename(targetPath)

            return 203, filename

        except:
            return 402, None

    # endregion

    # region Turkish Upper

    def turkishUpper(self, text):
        
        trMap = {
            'i': 'İ',
            'ş': 'Ş',
            'ğ': 'Ğ',
            'ü': 'Ü',
            'ö': 'Ö',
            'ç': 'Ç'
        }

        return ''.join([trMap.get(c, c.upper()) for c in text])

    # endregion

# endregion