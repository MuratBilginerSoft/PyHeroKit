# region Import Packages

from MidWare.FileProcess.ReadConfigJson.ReadConfigJson import ReadConfigJson
from MidWare.Settings.OutputMethod.OutputMethod import OutputMethod
from MidWare.Settings.Language.Language import Language
from Promt.Starter.RunPromt.RunPromt import RunPromt

# endregion

# region Start

language, outputMethod, outputPath = ReadConfigJson().main()

if language not in ['English', 'Türkçe']:
    Language().main()

if outputMethod not in ['Terminal', 'File']:
    OutputMethod().main()

RunPromt().main()

# endregion
