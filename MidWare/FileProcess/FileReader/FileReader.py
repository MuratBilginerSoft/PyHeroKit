# region Import Packages

import json

# endregion

# region Class FileReader

class FileReader:

    # region Init

    def __init__(self):
        pass

    # endregion

    # region Main

    def main(self, fileType, filePath):
        
        if fileType == 'txt':
            return self.txtRead(filePath)

        elif fileType == 'json':
            return self.jsonRead(filePath)
        
        else:
            return None
    
    # endregion
        
    # region Txt Reader
    
    def txtRead(self, FilePath):

        with open(FilePath, 'r', encoding="utf-8") as sourceFile:
            text = sourceFile.read()
        
        return text

    # endregion

    # region Json Reader
    
    def jsonRead(self, FilePath):

        with open(FilePath, 'r', encoding="utf-8") as sourceFile:
            data = json.load(sourceFile)

        return data
    
    # endregion

# endregion