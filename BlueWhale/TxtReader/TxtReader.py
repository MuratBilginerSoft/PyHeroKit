import os

# region TxtReader Class

class TxtReader:

    # region DocString

    """
    """

    # endregion

    # region Init

    def __init__(self):
        pass

    # endregion

    # region Main

    def main(self, sourcePath=None):

        return self.txtReader(sourcePath)

    # endregion

    # region Txt Reader

    def txtReader(self, sourcePath): 

        if not os.path.exists(sourcePath):
            return 403
        
        _, extension = os.path.splitext(sourcePath)

        if extension.lower() != '.txt':
            return 401
        
        try:
            with open(sourcePath, 'r', encoding="utf-8") as sourceFile:
                text = sourceFile.read()
            
            return text

        except:
            return 402

    # endregion

# endregion