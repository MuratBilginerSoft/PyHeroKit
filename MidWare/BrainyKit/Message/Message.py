# region Import Packages

from Utils.Languages.English import Messages as EngMessages
from Utils.Languages.Türkçe import Messages as TrMessages
from Utils.Sessions.Sessions import Sessions    

# endregion

# region Message Class

class Message:

    # region Init

    def __init__(self) -> None:
        pass
    
    # endregion

    # region Main

    def main(self):

        language = Sessions.language
        message = EngMessages()

        if language == 'Türkçe':
            message = TrMessages()
        
        Sessions.processes = message.process
        Sessions.system = message.system
        Sessions.menu = message.menu
        Sessions.info = message.info

    # endregion
        
    # region Message Language
        
    def messageLanguage(self):

        processes = Sessions.processes
        system = Sessions.system
        menu = Sessions.menu
        info = Sessions.info

        return processes, system, menu, info

    # endregion

# endregion