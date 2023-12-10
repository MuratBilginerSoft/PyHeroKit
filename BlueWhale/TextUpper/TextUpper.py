import os

# region TextUpper Class

class TextUpper:

    # region DocString

    """
    """

    # endregion

    # region Init

    def __init__(self):
        pass

    # endregion

    # region Main

    def main(self, choice=0, text=None, sourcePath=None, targetPath=None):
        
        if choice == 1:
            return self.stringTextUpper(text)
        elif choice == 2:
            return self.fileTextUpper(sourcePath, targetPath)

    # endregion

    # region String Text Upper

    def stringTextUpper(self, text): 
        return self.turkishUpper(text)

    # endregion

    # region File Text Upper

    def fileTextUpper(self, sourcePath, targetPath):

        _, extension = os.path.splitext(sourcePath)

        if extension.lower() != '.txt':
            return 401
        
        try:
            with open(sourcePath, 'r', encoding="utf-8") as sourceFile:
                text = sourceFile.read()
        
            resultText = self.turkishUpper(text)

            with open(targetPath, 'w', encoding="utf-8") as targetFile:
                targetFile.write(resultText)
            
            return 201

        except:
            return 402

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