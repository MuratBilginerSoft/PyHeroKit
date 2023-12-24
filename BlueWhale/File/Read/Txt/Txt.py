# region Import Packages

from MidWare.FileProcess.FileControl.FileControl import FileControl
from MidWare.FileProcess.FileReader.FileReader import FileReader
from MidWare.FileProcess.FileCreate.FileCreate import FileCreate
from Utils.Sessions.Sessions import Sessions

# endregion

# region TxtReader Class

class ReaderTxt:

    # region DocString

    """
    """

    # endregion

    # region Init

    def __init__(self):

        # region Create Objects

        self.FileControls = FileControl()
        self.FileReaders = FileReader()
        self.FileCreates = FileCreate()

        # endregion

        # region Set Sessions

        self.__outputMethod = Sessions.outputMethod

        # endregion

    # endregion

    # region Main

    def main(self, sourcePath=None):

        return self.txtReader(sourcePath)

    # endregion

    # region Txt Reader

    def txtReader(self, sourcePath): 

        fileStatus, extensionStatus = self.FileControls.main(sourcePath, '.txt')

        if fileStatus == 303:
            return 403, None
        if extensionStatus == 304:
            return 401, None

        try:
            text = None
            text = self.FileReaders.txtRead(sourcePath)

            if self.__outputMethod == 'Terminal':

                return 202, text
            
            elif self.__outputMethod == 'File':

                return 202, text
        
            else:
                return 402, None

        except:
            return 402, None

    # endregion

# endregion