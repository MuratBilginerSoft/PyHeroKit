# region Import Packages

import os

# endregion

# region FileControl Class

class FileControl:

    # region Init

    def __init__(self) -> None:
        pass

    # endregion

    # region Main

    def main(self, filePath: str, extension: str):

        fileStatus = self.fileCheck(filePath)
        extensionStatus = self.extensionCheck(filePath, extension)

        return fileStatus, extensionStatus
    
    # endregion

    # region File Check
        
    def fileCheck(self, filePath: str):

        if not os.path.exists(filePath):
            return 303
        
        return 301

    # endregion

    # region Extension Check
    
    def extensionCheck(self, filePath: str, extension: str):

        _, extension = os.path.splitext(filePath)

        if extension.lower() != '.txt':
            return 304

        return 302

    # endregion
    
# endregion