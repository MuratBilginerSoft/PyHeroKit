# region Import Packages

import datetime
import os

from Utils.Sessions.Sessions import Sessions

# endregion

# region FileCreate Class

class FileCreate:

    # region Init

    def __init__(self):

        self.__outputPath = Sessions.outputPath

    # endregion
        
    # region Main
        
    def main(self, text, filePrefix=''):

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        outputPath = os.path.join(self.__outputPath)

        if not os.path.exists(outputPath):
            os.makedirs(outputPath)

        filename = os.path.join(outputPath, f"{filePrefix}_{timestamp}.txt") 

        with open(filename, 'w', encoding="utf-8") as targetFile:
            targetFile.write(text)
        
        return filename
    
    # endregion

    # region Write File

    def writeFile(self, sourcePath, text):

        with open(sourcePath, 'w', encoding="utf-8") as targetFile:
            targetFile.write(text)
    
    # endregion

# endregion