# region Import Packages

import string

from MidWare.FileProcess.FileControl.FileControl import FileControl
from MidWare.FileProcess.FileReader.FileReader import FileReader
from MidWare.FileProcess.FileCreate.FileCreate import FileCreate
from MidWare.BrainyKit.Message.Message import Message
from Utils.Sessions.Sessions import Sessions

# endregion

# region CharacterCounter Class

class CharacterCounter:

    # region DocString

    """
    """

    # endregion

    # region Init

    def __init__(self):
        
        # region Create Objects

        self.FileControls = FileControl()
        self.FileCreates = FileCreate()
        self.FileReaders = FileReader()
        self.Messages = Message()

        # endregion

        # region Set Sessions

        self.__outputMethod = Sessions.outputMethod
        
        # endregion

    # endregion

    # region Main

    def main(self, text=""):

        return self.countLetter(text)

    # endregion

    # region Txt Reader

    def countLetter(self, text): 

        _, system, _, _ = self.Messages.messageLanguage()

        try:
            allCharacters = len(text)
            letters = len([c for c in text if c.isalpha()])
            spaces = text.count(' ')
            punctuation = len([c for c in text if c in string.punctuation])

            text = f"{'*'*30}\n\n{system['8']['message']}{allCharacters}\n{system['9']['message']}{letters}\n{system['10']['message']}{spaces}\n{system['11']['message']}{punctuation}\n\n{'*'*30}\n\n{text}"

            if self.__outputMethod == 'Terminal':

                return 202, text
            
            elif self.__outputMethod == 'File':

                fileName = self.FileCreates.main(text, 'Letter Counter')
                return 203, fileName
        
            else:
                return 402, None
        
        except Exception:
            return 402, None

    # endregion

# endregion