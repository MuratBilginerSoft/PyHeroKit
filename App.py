from MidWare.ReadLanguageJson.ReadLanguageJson import ReadLanguageJson
from MidWare.SelectLanguage.SelectLanguage import SelectLanguage
from BlueWhale.UserPromt.UserPromt import UserPromt

language = ReadLanguageJson().main()
SelectLanguage.language = language

if language not in ['English', 'Türkçe']:
    
    SelectLanguage().main()  
    UserPromt().main()

else:
    UserPromt().main()