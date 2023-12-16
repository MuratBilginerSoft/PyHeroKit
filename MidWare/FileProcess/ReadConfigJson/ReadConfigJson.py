# region Import Packages

from MidWare.Settings.OutputMethod.OutputMethod import OutputMethod
from MidWare.FileProcess.FileReader.FileReader import FileReader
from MidWare.BrainyKit.Message.Message import Message

from Utils.Sessions.Sessions import Sessions

# endregion

# region Class ReadConfigJson

class ReadConfigJson:

    # region DocString

    """

    This module contains the ReadLanguageJson class which is used to read the language setting from a JSON configuration file.

    The main method of the class opens the configuration file, reads the JSON data, and returns the current language setting.

    """

    # endregion

    # region Init

    def __init__(self):

        # region Create Objects

        self.FileReaders = FileReader() 

        # endregion

        # region Class Variables

        self.__pyConfigPath = 'Utils/Data/Config/PyConfig.json'

        # endregion

    # endregion
    
    # region Main 
        
    def main(self):

        data = self.FileReaders.jsonRead(self.__pyConfigPath)

        outputMethod = data.get('outputMethod', '')
        outputPath = data.get('outputPath', '')
        language = data.get('language', '')

        Sessions.language = language
        Sessions.outputMethod = outputMethod
        Sessions.outputPath = outputPath

        Message().main()

        return language, outputMethod, outputPath

    # endregion

# endregion